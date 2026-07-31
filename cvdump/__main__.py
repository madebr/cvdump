#!/usr/bin/env python

import argparse
import pathlib
import zipfile

from cvdump.dump_tpi import dump_tpi
from cvdump.msf import MsfFile
from cvdump.kaitai.dbi_stream import DbiStream
from cvdump.kaitai.tpi_stream import TpiStream

import kaitaistruct

def main():
    parser = argparse.ArgumentParser(
        description="Dump PDB to stdout",
        allow_abbrev=False,
    )
    parser.add_argument("--modules", "-m", dest="dump_modules", action="store_true", help="Dump modules")
    parser.add_argument("--seccontrib", dest="dump_seccontrib", action="store_true", help="Dump section contributions")
    parser.add_argument("--segment-map", "-x", dest="dump_segment_map", action="store_true", help="Dump segment map")
    parser.add_argument("--source-files", "-sf", dest="dump_source_files", action="store_true", help="Dump source files")
    parser.add_argument("--types", "-t", dest="dump_types", action="store_true", help="Dump types")
    parser.add_argument("--create-zip", type=pathlib.Path, help="Write streams to zip")
    parser.add_argument("pdb_path", metavar="pdb", type=pathlib.Path, help="PDB path")
    args = parser.parse_args()

    with args.pdb_path.open("rb") as f:
        msf_file = MsfFile.create(f)

        dbi = None
        tpi = None
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

        if args.create_zip:
            with zipfile.ZipFile(args.create_zip, "w") as zf:
                w = len(f"{msf_file.count_streams:d}")
                for i in range(1, msf_file.count_streams):
                    zip_entry_name = f"{i:0{w}d}.bin"
                    zf.writestr(zip_entry_name, msf_file.create_stream(i).read())

        if args.dump_modules:
            print()
            print("*** MODULES")
            print()
            for modi, mod_info in enumerate(get_dbi().module_info.entries, 1):
                extra = f" \"{mod_info.module_name}\"" if mod_info.object_name != mod_info.module_name else ""
                print(f"{modi:04X} \"{mod_info.object_name}\"{extra}")

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
            # If this assertion fails, there are more then 0x10000 source files
            # FIXME: calculate this in ksy description?
            assert sum(dbi.source_info.module_file_counts) == dbi.source_info.count_source_files

            print()
            print("*** SOURCE FILES")
            print()

            start_name_index = 0
            for module_index in range(dbi.source_info.count_modules):
                module_source_count = dbi.source_info.module_file_counts[module_index]
                module_data = dbi.module_info.entries[module_index]  # dbi.source_info.module_indices[module_index]]

                print(
                    f"** Module: \"{module_data.module_name}\" from \"{module_data.object_name}\"")  # module_index, module_source_count)
                print()

                for j in range(dbi.source_info.module_file_counts[module_index]):
                    name_offset = dbi.source_info.file_name_offsets[start_name_index + j]
                    # Pascal string
                    len_string = dbi.source_info.buffer[name_offset]
                    name = dbi.source_info.buffer[name_offset + 1:name_offset + 1 + len_string].decode("ascii")
                    print(f"  {j:>4} {name} (None)")
                if dbi.source_info.module_file_counts[module_index]:
                    print()
                start_name_index += dbi.source_info.module_file_counts[module_index]

        if args.dump_types:
            dump_tpi(get_tpi())

if __name__ == "__main__":
    raise SystemExit(main())
