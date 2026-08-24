#!/usr/bin/env python

import argparse
import binascii
import datetime
import itertools
import pathlib
import enum
import uuid
import zipfile

from cvdump.dump_tpi import dump_ipi, dump_tpi
from cvdump.dump_symbol import dump_symbol, MachineConfig
from cvdump.machine import Machine
from cvdump.msf import MsfFile
from cvdump.kaitai.c13_line_stream import C13LineStream
from cvdump.kaitai.dbi_stream import DbiStream
from cvdump.kaitai.info_stream import InfoStream
from cvdump.kaitai.modi_stream import ModiStream
from cvdump.kaitai.names_stream import NamesStream
from cvdump.kaitai.tpi_stream import TpiStream

import kaitaistruct

class PDBFeatureSig(enum.Enum):
    VC110 = 20091201
    VC140 = 20140508
    NoTypeMerge = 0x4d544f4e
    MinimalDebugInfo = 0x494e494d


class CV_SourceChksum_t(enum.IntEnum):
    CHKSUM_TYPE_NONE = 0
    CHKSUM_TYPE_MD5 = 1
    CHKSUM_TYPE_SHA1 = 2
    CHKSUM_TYPE_SHA_256 = 3

CHECKSUM_TO_NAME: dict[CV_SourceChksum_t, str] = {
    CV_SourceChksum_t.CHKSUM_TYPE_NONE: "None",
    CV_SourceChksum_t.CHKSUM_TYPE_MD5: "MD5",
    CV_SourceChksum_t.CHKSUM_TYPE_SHA1: "SHA1",
    CV_SourceChksum_t.CHKSUM_TYPE_SHA_256: "SHA_256",
}


def get_hash_name(hash_id: int) -> str:
    try:
        return CHECKSUM_TO_NAME.get(CV_SourceChksum_t(hash_id))
    except (IndexError, ValueError):
        return f"???({hash_id:02X})"


def main():
    parser = argparse.ArgumentParser(
        description="Dump PDB to stdout",
        allow_abbrev=False,
    )
    parser.add_argument("--ls",  dest="list_streams", action="store_true", help="List MSF streams")
    parser.add_argument("--info",  dest="info", action="store_true", help="PDB Information")
    parser.add_argument("-l",  dest="dump_lines", action="store_true", help="Source lines")
    parser.add_argument("--names",  dest="dump_names", action="store_true", help="Dump Names stream")
    parser.add_argument("--modules", "-m", dest="dump_modules", action="store_true", help="Dump modules")
    parser.add_argument("--seccontrib", dest="dump_seccontrib", action="store_true", help="Dump section contributions")
    parser.add_argument("--segment-map", "-x", dest="dump_segment_map", action="store_true", help="Dump segment map")
    parser.add_argument("--source-files", "-sf", dest="dump_source_files", action="store_true", help="Dump source files")
    parser.add_argument("-id", dest="dump_id", action="store_true", help="Dump types (TPI stream)")
    parser.add_argument("--types", "-t", dest="dump_types", action="store_true", help="Dump IDs (IPI stream)")
    parser.add_argument("--symbols", "-s", dest="dump_symbols", action="store_true", help="Dump symbols")
    parser.add_argument("--create-zip", type=pathlib.Path, help="Write streams to zip")
    parser.add_argument("pdb_path", metavar="pdb", type=pathlib.Path, help="PDB path")
    args = parser.parse_args()

    with args.pdb_path.open("rb") as f:
        msf_file = MsfFile.create(f)

        dbi = None
        tpi = None
        gsi = None
        info = None
        named_stream_map = None
        named_stream_map_initialized = False
        names = None
        names_initialized = False
        name_index_to_name = None
        name_offset_to_name = None
        module_streams = {}
        machine = None

        def get_dbi() -> DbiStream:
            nonlocal dbi
            if not dbi:
                dbi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.DBI_STREAM_INDEX))
                dbi = DbiStream(dbi_kaitai_stream)
            return dbi
        def get_tpi() -> TpiStream:
            nonlocal tpi
            if not tpi:
                tpi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.TPI_STREAM_INDEX))
                tpi = TpiStream(tpi_kaitai_stream)
            return tpi
        def get_ipi() -> TpiStream:
            nonlocal tpi
            if not tpi:
                tpi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.IPI_STREAM_INDEX))
                tpi = TpiStream(tpi_kaitai_stream)
            return tpi
        # def get_gsi() -> GsiStream:
        #     nonlocal gsi
        #     if not gsi:
        #         dbi = get_dbi()
        #         gsi = dbi.header.global_symbol_stream
        #         print(f"{gsi=}")
        #         # dbi = get_dbi()
        #         # # sym_rec_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(dbi.header.global_symbol_stream))
        #         # gsi_taikai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(dbi.header.global_symbol_stream))
        #         # gsi = GsiStream(gsi_taikai_stream)
        #     return gsi
        def get_info() -> InfoStream:
            nonlocal info
            if not info:
                info_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(1))
                info = InfoStream(info_kaitai_stream)
            return info
        def get_named_stream_map() -> dict[str, int] | None:
            nonlocal named_stream_map
            nonlocal named_stream_map_initialized
            if not named_stream_map_initialized:
                info = get_info()
                named_stream_map = {}
                # WRONG: use extra bits to check whether key is present
                # also verify whether it is possible to build a map (and only lookup)
                if hasattr(info, "contents_vc50"):
                    for entry in info.contents_vc50.entries:
                        if (pos_end := info.contents_vc50.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc50.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc50.string_buffer[entry.key:]
                        named_stream_map[name.decode()] = entry.value
                if hasattr(info, "contents_vc98"):
                    for entry in info.contents_vc98.entries:
                        if (pos_end := info.contents_vc98.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc98.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc98.string_buffer[entry.key:]
                        named_stream_map[name.decode()] = entry.value
                if hasattr(info, "contents_vc70"):
                    for entry in info.contents_vc70.entries:
                        if (pos_end := info.contents_vc70.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc70.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc70.string_buffer[entry.key:]
                        named_stream_map[name.decode()] = entry.value
            named_stream_map_initialized = True
            return named_stream_map
        def get_names() -> NamesStream:
            nonlocal names
            nonlocal names_initialized
            if not names_initialized:
                named_stream_map = get_named_stream_map()
                if named_stream_map:
                    names_stream_index = named_stream_map.get("/names")
                    if names_stream_index:
                        names_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(names_stream_index))
                        names = NamesStream(names_kaitai_stream)
            names_initialized = True
            return names

        def process_namemap() ->dict[int, str]:
            nonlocal name_index_to_name
            nonlocal name_offset_to_name
            name_index_to_name = {}
            name_offset_to_name = {}
            names = get_names()
            if names.hash_version == 1:
                i = 0
                string_start = 0
                while string_start is not None:
                    string_end = names.string_buffer.find(0, string_start)
                    if string_end == -1:
                        text = names.string_buffer[string_start:]
                        next_string_start = None
                    else:
                        text = names.string_buffer[string_start:string_end]
                        next_string_start = string_end + 1
                    name_index_to_name[i] = text
                    name_offset_to_name[string_start] = text
                    string_start = next_string_start
                    i += 1
            else:
                print(f"Unsupported names hash version ({names.hash_version}) (PLEASE SHARE THIS PDB!)")
                raise ValueError
            return name_index_to_name

        def get_name_offset_to_name() -> dict[int, str]:
            nonlocal name_offset_to_name
            if name_offset_to_name is None:
                process_namemap()
            return name_offset_to_name

        def get_module_stream(module_index: int) -> ModiStream:
            nonlocal module_streams
            if module_index not in module_streams:
                dbi = get_dbi()
                dbi_module_info_entry = dbi.module_info.entries[module_index]
                stream_index = dbi_module_info_entry.debug_info_stream
                module_stream = None
                if stream_index != 0xffff:
                    symbols_size = dbi_module_info_entry.symbols_size
                    if hasattr(dbi_module_info_entry, "c11_line_size"):
                        c11_line_size = dbi_module_info_entry.c11_line_size
                        c13_line_size = dbi_module_info_entry.c13_line_size
                    else:
                        c11_line_size = dbi_module_info_entry.lines_size
                        c13_line_size = 0
                    module_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(stream_index))
                    module_stream = ModiStream(symbols_size=symbols_size, c11_line_size=c11_line_size, c13_line_size=c13_line_size, _io=module_kaitai_stream)
                module_streams[module_index] = module_stream
            return module_streams[module_index]
        def get_machine() -> Machine | None:
            nonlocal machine
            if machine is None:
                dbi = get_dbi()
                if hasattr(dbi.header, "new_header"):
                    machine = Machine(dbi.header.new_header.machine)
                    if machine == Machine.IMAGE_FILE_MACHINE_UNKNOWN:
                        machine = None
            return machine
        if args.create_zip:
            with zipfile.ZipFile(args.create_zip, "w") as zf:
                w = len(f"{msf_file.count_streams:d}")
                for i in range(1, msf_file.count_streams):
                    zip_entry_name = f"{i:0{w}d}.bin"
                    zf.writestr(zip_entry_name, msf_file.create_stream(i).read())

        if args.list_streams:
            print("*** MSF Stream info")
            print()
            print(f"Block size = {msf_file.block_size} (0x{msf_file.block_size:x})")
            print()
            print("Module streams")
            print("stream symbol      c11_line   c13_line   name")
            dbi = get_dbi()
            for modi, mod_info in enumerate(get_dbi().module_info.entries, 1):
                debug_info_stream = mod_info.debug_info_stream
                if debug_info_stream == 0xffff:
                    debug_info_stream = "n/a"
                if hasattr(mod_info, "c11_line_size"):
                    c11_line_size = mod_info.c11_line_size
                    c13_line_size = mod_info.c13_line_size
                else:
                    c11_line_size = mod_info.lines_size
                    c13_line_size = 0
                print(f"{debug_info_stream:>6} 0x{mod_info.symbols_size:08x}  0x{c11_line_size:08x} 0x{c13_line_size:08x} {mod_info.module_name}")
            for stream_index in range(len(msf_file.stream_sizes)):
                print()
                print(f"Stream {stream_index}:")
                print(f"     size: {msf_file.stream_sizes[stream_index]} (0x{msf_file.stream_sizes[stream_index]:x})")
                print(f"  indices:")#{' '.join(hex(b) for b in msf_file.stream_block_maps[stream_index])}")
                for batch in itertools.batched((hex(b) for b in msf_file.stream_block_maps[stream_index]), 10):
                    print("     ", " ".join(batch))

        if args.info:
            info = get_info()
            print()
            print("*** PDF INFORMATION:")
            print()
            print(f"  version: {info.version}")
            print(f"     time: {datetime.datetime.fromtimestamp(info.timestamp).strftime('%Y-%m-%d %H:%M:%S')} (0x{info.timestamp:08x})")
            if hasattr(info, "contents_vc50"):
                print("Stream map:")
                for stream_name, stream_index in get_named_stream_map().items():
                    print(f"{stream_name:>20}: {stream_index}")
            elif hasattr(info, "contents_vc98"):
                print("Stream map:")
                for stream_name, stream_index in get_named_stream_map().items():
                    print(f"{stream_name:>20}: {stream_index}")
            elif hasattr(info, "contents_vc70"):
                pdb_uuid = uuid.UUID(bytes_le=info.contents_vc70.uuid)
                print(f"     guid: {pdb_uuid}")
                print(f"      age: {info.contents_vc70.age}")
                print("Stream map:")
                for stream_name, stream_index in get_named_stream_map().items():
                    print(f"{stream_name:>20}: {stream_index}")
                print(f"Features: {', '.join(PDBFeatureSig(f).name for f in info.contents_vc70.features)}")
            print()

        if args.dump_names:
            print()
            print("*** NAMES:")
            print()
            names = get_names()
            if not names:
                print("/names stream not found")
            else:
                print(f"   Signature = 0x{names.signature:08x}")
                print(f"Hash Version = 0x{names.hash_version:x}")
                if names.hash_version == 1:
                    print(f"String count = {names.amount_of_strings}")
                    print(f"Bucket count = {names.bucket_count}")
                    print("Strings:")
                    print("index    offset   text")
                    i = 0
                    string_start = 0
                    while string_start is not None:
                        string_end = names.string_buffer.find(0, string_start)
                        if string_end == -1:
                            text = names.string_buffer[string_start:]
                            next_string_start = None
                        else:
                            text = names.string_buffer[string_start:string_end]
                            next_string_start = string_end + 1
                        print(f"{i:<8} {string_start:08x} \"{text.decode('ascii')}\"")
                        string_start = next_string_start
                        i += 1
                else:
                    print("Unsupported hash version (PLEASE SHARE THIS PDB!)")

        if args.dump_modules:
            print()
            print("*** MODULES")
            print()
            for module_index, mod_info in enumerate(get_dbi().module_info.entries, 1):
                extra = f" \"{mod_info.module_name}\"" if mod_info.object_name != mod_info.module_name else ""
                print(f"{module_index:04X} \"{mod_info.object_name}\"{extra}")

        if args.dump_lines:
            print()
            print("*** LINES")
            dbi = get_dbi()
            process_namemap()
            for module_index, mod_info in enumerate(dbi.module_info.entries):
                checksums = {}

                print()
                print(f"** Module: \"{mod_info.module_name}\"")
                module_stream = get_module_stream(module_index)
                found_checksum = False
                for subsection in module_stream.c13_line_info.subsections:
                    match subsection.header.type:
                        case C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                            for cksum in subsection.contents.checksums:
                                checksums[cksum.pos] = cksum
                            found_checksum = True
                    if found_checksum:
                        break

                for subsection in module_stream.c13_line_info.subsections:
                    match subsection.header.type:
                        case C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                            pass
                        case C13LineStream.DebugSSubsectionType.debug_s_lines:
                            for table_i, table in enumerate(subsection.contents.tables.items):
                                try:
                                    cksum = checksums[table.fileid]
                                except KeyError:
                                    raise
                                filename = name_offset_to_name[cksum.name_index].decode()
                                start = subsection.contents.off_con if table_i == 0 else (subsection.contents.off_con + table.lines[0].offset)
                                end = (subsection.contents.off_con + subsection.contents.count_con) if table_i + 1 == len(subsection.contents.tables.items) else (subsection.contents.off_con + subsection.contents.tables.items[table_i + 1].lines[0].offset)
                                print()
                                print(f"  {filename} ({get_hash_name(cksum.hash_type)}: {binascii.b2a_hex(cksum.hash).decode().upper()}), {subsection.contents.seg_con:04X}:{start:08X}-{end:08X}, line/addr pairs = {table.count_lines}")
                                print()
                                for i, line_item in enumerate(table.lines):
                                    if line_item.line_number_start in (0xfeefee, 0xf00f00):
                                        print(f"  {line_item.line_number_start:x} {subsection.contents.off_con+line_item.offset:08X}", end="")
                                    else:
                                        print(f"  {line_item.line_number_start:5} {subsection.contents.off_con+line_item.offset:08X}", end="")
                                    if i % 4 == 3 or i == len(table.lines) - 1:
                                        print()
                        case C13LineStream.DebugSSubsectionType.debug_s_inlineelines:
                            # FIXME: display for -inll
                            pass
                        case _:
                            raise ValueError


        if args.dump_symbols:
            print()
            print("*** SYMBOLS")
            dbi = get_dbi()
            for module_index, mod_info in enumerate(dbi.module_info.entries):
                machine_config = MachineConfig(machine=get_machine())

                print()
                print(f"** Module: \"{mod_info.module_name}\"")
                module_stream = get_module_stream(module_index)
                if module_stream is None:
                    continue
                print()
                if mod_info.symbols_size > 0:
                    for symbol in module_stream.symbols.entries:
                        dump_symbol(symbol, machine_config=machine_config, module_info=mod_info)

        if args.dump_seccontrib:
            print()
            print("*** SECTION CONTRIBUTIONS")
            print()
            print("  Imod  Address        Size      Characteristics")
            for sec_con in get_dbi().section_contribution.entries:
                print(f"  {sec_con.module_index+1:04X}  {sec_con.section_index:04X}:{sec_con.offset:08X}  {sec_con.size:08X}  {sec_con.characteristics:08X}")

        if args.dump_segment_map:
            print()
            print("*** SEGMENT MAP")
            print()
            print("Sec  flags  ovl   grp   frm sname cname    offset    cbSeg")
            for i, smap_item in enumerate(get_dbi().section_map.rg_desc, 1):
                print(f" {i:02X}  {smap_item.f_all:04X}  {smap_item.ovl:04X}  {smap_item.group:04X}  {smap_item.frame:04x}  {smap_item.i_seg_name:04x}  {smap_item.i_class_name:04x}  {smap_item.offset:08x} {smap_item.cb_seg:08x}")

        if args.dump_source_files:
            dbi = get_dbi()

            print()
            print("*** SOURCE FILES")
            print()

            actual_count_source_files = sum(dbi.source_info.module_file_counts)
            if actual_count_source_files != dbi.source_info.count_source_files:
                print("* Total amount of sourc files truncated")
                print()
            # If this assertion fails, there are more then 0x10000 source files
            assert actual_count_source_files == dbi.source_info.count_source_files, "current kaitai description does not support truncated source file count"

            start_name_index = 0
            for module_index in range(dbi.source_info.count_modules):
                module_source_count = dbi.source_info.module_file_counts[module_index]
                module_data = dbi.module_info.entries[module_index]  # dbi.source_info.module_indices[module_index]]

                print(
                    f"** Module: \"{module_data.module_name}\" from \"{module_data.object_name}\"")  # module_index, module_source_count)
                print()

                for j in range(module_source_count):
                    name_offset = dbi.source_info.file_name_offsets[start_name_index + j]
                    if dbi.header.is_new_header:
                        end_name = dbi.source_info.buffer.find(b'\0', name_offset)
                        if end_name == -1:
                            end_name = None
                        name = dbi.source_info.buffer[name_offset:end_name]
                    else:
                        # Pascal string
                        len_string = dbi.source_info.buffer[name_offset]
                        name = dbi.source_info.buffer[name_offset + 1:name_offset + 1 + len_string].decode("ascii")
                    # FIXME: add hash instead of None.
                    #        e.g. SHA_256: 991883893134C8ECBE6AF8335DF0781BFB779C11684B3367DEF514136241B866
                    print(f"  {j:>4} {name.decode('ascii')} (HASH TBD)")
                if module_source_count:
                    print()
                start_name_index += module_source_count

        if args.dump_types:
            dump_tpi(get_tpi())

        if args.dump_id:
            # FIXME: IPI stream is not available on small PDB's
            dump_ipi(get_ipi(), get_name_offset_to_name())

if __name__ == "__main__":
    raise SystemExit(main())
