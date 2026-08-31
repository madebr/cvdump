#!/usr/bin/env python

import argparse
import binascii
import datetime
import io
import itertools
import pathlib
import enum
import uuid
import zipfile

from cvdump.dump_tpi import dump_ipi, dump_tpi
from cvdump.dump_symbol import dump_symbol, MachineConfig
from cvdump.machine import Machine
from cvdump.msf import MsfFile
from cvdump.names import StringTable
from cvdump.kaitai.c13_line_stream import C13LineStream
from cvdump.kaitai.cv_symbol_stream import CvSymbolStream
from cvdump.kaitai.dbi_stream import DbiStream
from cvdump.kaitai.psi_gsi import PsiGsi
from cvdump.kaitai.info_stream import InfoStream
from cvdump.kaitai.modi_stream import ModiStream
from cvdump.kaitai.names_stream import NamesStream
import cvdump.kaitai.omf
from cvdump.kaitai.tpi_stream import TpiStream

import kaitaistruct

class PDBFeatureSig(enum.Enum):
    VC110 = 20091201
    VC140 = 20140508
    NoTypeMerge = 0x4d544f4e
    MinimalDebugInfo = 0x494e494d



def main():
    parser = argparse.ArgumentParser(
        description="Dump PDB to stdout",
        allow_abbrev=False,
    )
    parser.add_argument("--ls",  dest="list_streams", action="store_true", help="List MSF streams")
    parser.add_argument("--info",  dest="dump_info", action="store_true", help="PDB Information")
    parser.add_argument("-g",  dest="dump_globals", action="store_true", help="Global symbols")
    parser.add_argument("-p",  dest="dump_publics", action="store_true", help="Public symbols")
    parser.add_argument("-l",  dest="dump_lines", action="store_true", help="Source lines")
    parser.add_argument("--names",  dest="dump_names", action="store_true", help="Dump Names stream")
    parser.add_argument("--modules", "-m", dest="dump_modules", action="store_true", help="Dump modules")
    parser.add_argument("--seccontrib", dest="dump_seccontrib", action="store_true", help="Dump section contributions")
    parser.add_argument("--segment-map", "-x", dest="dump_segment_map", action="store_true", help="Dump segment map")
    parser.add_argument("--source-files", "-sf", dest="dump_source_files", action="store_true", help="Dump source files")
    parser.add_argument("-id", dest="dump_id", action="store_true", help="Dump types (TPI stream)")
    parser.add_argument("--types", "-t", dest="dump_types", action="store_true", help="Dump IDs (IPI stream)")
    parser.add_argument("--symbols", "-s", dest="dump_symbols", action="store_true", help="Dump symbols (from modules)")
    parser.add_argument("--symbol-records", dest="dump_symbol_records", action="store_true", help="Dump symbols (from symbol record stream)")
    parser.add_argument("--create-zip", type=pathlib.Path, help="Write streams to zip")
    parser.add_argument("pdb_path", metavar="pdb", type=pathlib.Path, help="PDB path")
    args = parser.parse_args()

    with args.pdb_path.open("rb") as f:
        msf_file = MsfFile.create(f)

        private_dbi = None
        private_ipi = None
        private_tpi = None
        private_symbol_record_stream_symbols = None
        private_gsi = None
        private_psi = None
        private_info = None
        private_named_stream_map = None
        private_named_stream_map_initialized = False
        private_names = None
        private_names_initialized = False
        private_string_table = None
        # private_name_index_to_name = None
        # private_name_offset_to_name = None
        private_module_streams = {}
        private_machine = None

        def get_dbi() -> DbiStream:
            nonlocal private_dbi
            if not private_dbi:
                dbi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.DBI_STREAM_INDEX))
                private_dbi = DbiStream(dbi_kaitai_stream)
            return private_dbi
        def get_tpi() -> TpiStream:
            nonlocal private_tpi
            if not private_tpi:
                tpi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.TPI_STREAM_INDEX))
                private_tpi = TpiStream(tpi_kaitai_stream)
            return private_tpi
        def get_ipi() -> TpiStream:
            nonlocal private_ipi
            if not private_ipi:
                tpi_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(MsfFile.IPI_STREAM_INDEX))
                private_ipi = TpiStream(tpi_kaitai_stream)
            return private_ipi
        def get_symbol_record_stream_symbols() -> CvSymbolStream:
            nonlocal private_symbol_record_stream_symbols
            if not private_symbol_record_stream_symbols:
                dbi = get_dbi()
                private_symbol_record_stream_symbols = CvSymbolStream(delta_pos=0, align4=True, _io=kaitaistruct.KaitaiStream(msf_file.create_stream(dbi.header.symbol_record_stream)))
            return private_symbol_record_stream_symbols
        def get_gsi_records() -> PsiGsi.PdbHashRecordArray:
            nonlocal private_gsi
            if not private_gsi:
                dbi = get_dbi()
                gsi_stream_index = dbi.header.global_symbol_stream
                gsi_stream = msf_file.create_stream(gsi_stream_index)
                ks = kaitaistruct.KaitaiStream(gsi_stream)
                try:
                    header = PsiGsi.NewHeader(ks)
                    records_byte_stream = io.BytesIO(gsi_stream.read(header.hash_records_byte_size))
                    private_gsi = PsiGsi.PdbHashRecordArray(kaitaistruct.KaitaiStream(records_byte_stream))
                except kaitaistruct.ValidationFailedError:
                    gsi_stream.seek(0)
                    private_gsi = PsiGsi.LimitedPdbHashRecordArray(ks)
            return private_gsi
        def get_psi_records() -> PsiGsi.PdbHashRecordArray:
            nonlocal private_psi
            if not private_psi:
                dbi = get_dbi()
                psi_stream_index = dbi.header.public_symbol_stream
                psi_stream = msf_file.create_stream(psi_stream_index)
                ks = kaitaistruct.KaitaiStream(psi_stream)
                psi_header = PsiGsi.PsiStreamHeader(ks)
                p = psi_stream.tell()
                try:
                    header = PsiGsi.NewHeader(ks)
                    records_byte_stream = io.BytesIO(psi_stream.read(header.hash_records_byte_size))
                    private_psi = PsiGsi.PdbHashRecordArray(kaitaistruct.KaitaiStream(records_byte_stream))
                except kaitaistruct.ValidationFailedError:
                    psi_stream.seek(p)
                    private_psi = PsiGsi.LimitedPdbHashRecordArray(ks)
            return private_psi
        def get_info() -> InfoStream:
            nonlocal private_info
            if not private_info:
                info_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(1))
                private_info = InfoStream(info_kaitai_stream)
            return private_info
        def get_named_stream_map() -> dict[str, int] | None:
            nonlocal private_named_stream_map
            nonlocal private_named_stream_map_initialized
            if not private_named_stream_map_initialized:
                info = get_info()
                private_named_stream_map = {}
                # WRONG: use extra bits to check whether key is present
                # also verify whether it is possible to build a map (and only lookup)
                if hasattr(info, "contents_vc50"):
                    for entry in info.contents_vc50.entries:
                        if (pos_end := info.contents_vc50.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc50.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc50.string_buffer[entry.key:]
                        private_named_stream_map[name.decode()] = entry.value
                if hasattr(info, "contents_vc98"):
                    for entry in info.contents_vc98.entries:
                        if (pos_end := info.contents_vc98.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc98.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc98.string_buffer[entry.key:]
                        private_named_stream_map[name.decode()] = entry.value
                if hasattr(info, "contents_vc70"):
                    for entry in info.contents_vc70.entries:
                        if (pos_end := info.contents_vc70.string_buffer.find(0, entry.key)) != -1:
                            name = info.contents_vc70.string_buffer[entry.key:pos_end]
                        else:
                            name = info.contents_vc70.string_buffer[entry.key:]
                        private_named_stream_map[name.decode()] = entry.value
            private_named_stream_map_initialized = True
            return private_named_stream_map
        def get_names() -> NamesStream:
            nonlocal private_names
            nonlocal private_names_initialized
            if not private_names_initialized:
                named_stream_map = get_named_stream_map()
                if named_stream_map:
                    names_stream_index = named_stream_map.get("/names")
                    if names_stream_index:
                        names_kaitai_stream = kaitaistruct.KaitaiStream(msf_file.create_stream(names_stream_index))
                        private_names = NamesStream(names_kaitai_stream)
            private_names_initialized = True
            return private_names

        def process_namemap() -> StringTable:
            nonlocal private_string_table
            # nonlocal private_name_index_to_name
            # nonlocal private_name_offset_to_name
            # private_name_index_to_name = {}
            # private_name_offset_to_name = {}
            names = get_names()
            if names:
                if names.hash_version == 1:
                    private_string_table = StringTable.from_bytes(names.string_buffer)
                else:
                    print(f"Unsupported names hash version ({names.hash_version}) (PLEASE SHARE THIS PDB!)")
                    raise ValueError
            return private_string_table

        def get_name_offset_to_name() -> dict[int, str]:
            string_table = process_namemap()
            return string_table._offset_to_name

        def get_module_stream(module_index: int) -> ModiStream:
            nonlocal private_module_streams
            if module_index not in private_module_streams:
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
                private_module_streams[module_index] = module_stream
            return private_module_streams[module_index]
        def get_machine() -> Machine | None:
            nonlocal private_machine
            if private_machine is None:
                dbi = get_dbi()
                if hasattr(dbi.header, "new_header"):
                    private_machine = Machine(dbi.header.new_header.machine)
                    if private_machine == Machine.IMAGE_FILE_MACHINE_UNKNOWN:
                        private_machine = None
            return private_machine
        if args.create_zip:
            with zipfile.ZipFile(args.create_zip, "w") as zf:
                w = len(f"{msf_file.count_streams:d}")
                for i in range(msf_file.count_streams):
                    zip_entry_name = f"{i:0{w}d}.bin"
                    zf.writestr(zip_entry_name, msf_file.create_stream(i).read())

        if args.list_streams:
            print("*** MSF Stream info")
            print()
            print("Blocks:")
            print(f"Block size = {msf_file.block_size} (0x{msf_file.block_size:x})")
            dbi = get_dbi()
            if msf_file.msf.is_big_msf:
                print(f"MSF free blockmap: {msf_file.msf.big_superblock.free_block_map_block}")
                print(f"MSF blockmap: {msf_file.msf.big_superblock.block_map_address}")
            else:
                print(f"MSF free blockmap: {msf_file.msf.small_superblock.free_block_map_block}")
            print()
            print("Streams:")
            print(f"TPI stream: {MsfFile.TPI_STREAM_INDEX}")
            print(f"DBI stream: {MsfFile.DBI_STREAM_INDEX}")
            print(f"IPI stream: {MsfFile.IPI_STREAM_INDEX}")
            print(f"Global symbol stream: {dbi.header.global_symbol_stream}")
            print(f"Public symbol stream: {dbi.header.public_symbol_stream}")
            print(f"Symbol record stream: {dbi.header.symbol_record_stream}")
            mfc_stream = None
            if hasattr(dbi.header, "new_header"):
                mfc_stream = dbi.header.new_header.mfc_type_server_stream
                if mfc_stream == 0:
                    mfc_stream = None
            print(f"MFC type server stream: {mfc_stream if mfc_stream is not None else 'n/a'}")
            nsm = get_named_stream_map()
            print("Named streams: ", end="")
            if nsm is None:
                print("none")
            else:
                print()
                for stream_name, stream_index in nsm.items():
                    print(f"  - '{stream_name}': {stream_index}")

            # FIXME: print named streams

            print()
            print("Module streams")
            print("   i stream symbol   c11_line c13_line name")
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
                print(f"{modi:4}){debug_info_stream:>6} 0x{mod_info.symbols_size:06x} 0x{c11_line_size:06x} 0x{c13_line_size:06x} {mod_info.module_name}")
            for stream_index in range(len(msf_file.stream_sizes)):
                print()
                print(f"Stream {stream_index}:")
                print(f"     size: {msf_file.stream_sizes[stream_index]} (0x{msf_file.stream_sizes[stream_index]:x})")
                print(f"  indices:")#{' '.join(hex(b) for b in msf_file.stream_block_maps[stream_index])}")
                for batch in itertools.batched((hex(b) for b in msf_file.stream_block_maps[stream_index]), 10):
                    print("     ", " ".join(batch))

        if args.dump_info:
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
                if module_stream:
                    if module_stream.c13_line_size:
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
                                    cvdump.dump_c13.dump_lines(subsection.contents)
                                    for table_i, table in enumerate(subsection.contents.tables.items):
                                        try:
                                            cksum = checksums[table.fileid]
                                        except KeyError:
                                            raise
                                        name_offset_to_name = get_name_offset_to_name()
                                        filename = name_offset_to_name[cksum.name_index]
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
                    elif module_stream.c11_line_size:
                        bs = io.BytesIO(module_stream.c11_line_info)
                        ks = kaitaistruct.KaitaiStream(bs)
                        sm = cvdump.kaitai.omf.Omf.OmfSourceModule(ks)

                        for ifile in range(sm.c_file):
                            bs.seek(sm.file_starts[ifile])
                            assert bs.tell() == sm.file_starts[ifile]
                            sf = cvdump.kaitai.omf.Omf.OmfSourceFile(ks)
                            for iseg in range(sf.c_seg):
                                bs.seek(sf.start_lines[iseg])
                                sl = cvdump.kaitai.omf.Omf.OmfSourceLine(ks)
                                print()

                                end = sf.ranges[iseg].end
                                # cvdump.exe adds 1 to range
                                end += 1

                                print(f"  {sf.name.text} (None), {sl.seg:04X}:{sf.ranges[iseg].begin:08X}-{end:08X}, line/addr pairs = {sl.count_lines}")

                                for i in range(sl.count_lines):
                                    if i % 4 == 0:
                                        print()
                                    print(f" {sl.lines[i]:6} {sl.offsets[i]:08X}", end="")
                                if sl.count_lines != 0:
                                    print()
                    else:
                        pass

        if args.dump_globals:
            print()
            print("*** GLOBALS")
            print()

            symbol_records = get_symbol_record_stream_symbols()
            symbol_record_lut = {}
            for symbol in symbol_records.entries:
                symbol_record_lut[symbol.pos] = symbol
            gsi_records = get_gsi_records()
            for record in gsi_records.entries:
                if record.offset_symbol_record_stream_plus_one in (0, 0xffffffff):
                    break
                symbol = symbol_record_lut[record.offset_symbol_record_stream_plus_one - 1]
                dump_symbol(symbol, None, None, dump_pos=False)

        if args.dump_publics:
            print()
            print("*** PUBLICS")
            print()

            symbol_records = get_symbol_record_stream_symbols()
            symbol_record_lut = {}
            for symbol in symbol_records.entries:
                symbol_record_lut[symbol.pos] = symbol
            psi_records = get_psi_records()
            for record in psi_records.entries:
                if record.offset_symbol_record_stream_plus_one in (0, 0xffffffff):
                    break
                symbol = symbol_record_lut[record.offset_symbol_record_stream_plus_one - 1]
                dump_symbol(symbol, None, None, dump_pos=False)

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

        if args.dump_symbol_records:
            print()
            print("*** SYMBOL RECORDS")
            dbi = get_dbi()
            symbol_records = get_symbol_record_stream_symbols()
            machine_config = MachineConfig(machine=get_machine())
            for symbol in symbol_records.entries:
                dump_symbol(symbol, machine_config=machine_config, module_info=None)

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
            dump_ipi(get_ipi(), process_namemap())

if __name__ == "__main__":
    raise SystemExit(main())
