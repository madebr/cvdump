#!/usr/bin/env python3

import argparse
import datetime
import io
import pathlib
import struct

import cvdump.kaitai.coff
import cvdump.kaitai.c13_line_stream
from cvdump.kaitai.c13_line_stream import C13LineStream
import cvdump.kaitai.tpi_stream
import cvdump.pe_coff
import cvdump.dump_c13
import cvdump.dump_symbol
import cvdump.machine
import cvdump.names
import cvdump.dump_tpi

import kaitaistruct
import capstone


def machine_to_capstone_arch(machine: cvdump.machine.Machine) -> tuple[int, int]:
    match machine:
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_I386:
            return capstone.CS_ARCH_X86, capstone.CS_MODE_32
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_AMD64:
            return capstone.CS_ARCH_X86, capstone.CX_MODE_64
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_ARMV7:
            return capstone.CS_ARCH_ARM, capstone.CX_MODE_32
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_ARM64:
            return capstone.CS_ARCH_ARM64, capstone.CX_MODE_64
        case _:
            raise ValueError



def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("coff", type=pathlib.Path)
    args = parser.parse_args()

    with args.coff.open("rb") as coff_file:
        coff = cvdump.kaitai.coff.Coff(kaitaistruct.KaitaiStream(coff_file))

        print(f"                Machine: {coff.header.machine.name.upper()}")
        print(f"     Number of sections: {coff.header.number_of_sections}")
        print(f"        Time date stamp: {datetime.datetime.fromtimestamp(coff.header.time_date_stamp).strftime('%Y-%m-%d %H:%M:%S')} (0x{coff.header.time_date_stamp:08x})")
        print(f"Pointer to Symbol Table: 0x{coff.header.pointer_to_symbol_table:08x}")
        print(f"      Number of symbols: {coff.header.number_of_symbols}")
        print(f"Size of optional header: 0x{coff.header.size_of_optional_header:04x}")
        print(f"        Characteristics: {cvdump.pe_coff.PeCoffCharacteristic(coff.header.characteristics)} (0x{coff.header.characteristics:04x})")

        string_table = None

        for section_i, section_header in enumerate(coff.section_headers):
            print()
            print(f"- Section {section_i}:")
            print(f"                    name: {section_header.name.decode('ascii')}")
            print(f"            virtual size: 0x{section_header.virtual_size:x}")
            print(f"         virtual address: 0x{section_header.virtual_address:x}")
            print(f"        size of raw data: 0x{section_header.size_of_raw_data:x}")
            print(f"     pointer of raw data: 0x{section_header.pointer_to_raw_data:x}")
            print(f"  pointer to relocations: 0x{section_header.pointer_to_relocations:x}")
            print(f"  pointer to linenumbers: 0x{section_header.pointer_to_linenumbers:x}")
            print(f"   number of relocations: {section_header.number_of_relocations}")
            print(f"   number of linenumbers: {section_header.number_of_linenumbers}")
            print(f"         characteristics: {cvdump.pe_coff.PeCoffSectionFlags(section_header.characteristics).name} (0x{section_header.characteristics:08x})")

            DIRECTIVE_CHARACTERISTICS = cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_LNK_INFO | cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_LNK_REMOVE
            CODE_CHARACTERISTICS = cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_MEM_READ | cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_MEM_EXECUTE | cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_CNT_CODE
            coff_file.seek(section_header.pointer_to_raw_data)
            section_raw_data = coff_file.read(section_header.size_of_raw_data)
            if section_header.name == b".drectve" and section_header.characteristics & DIRECTIVE_CHARACTERISTICS == DIRECTIVE_CHARACTERISTICS:
                print()
                print(f"    contents = '{section_raw_data.decode('ascii')}'")
            elif section_header.name == b".debug$S":
                machine_config = cvdump.dump_symbol.MachineConfig(machine=cvdump.machine.Machine(coff.header.machine))
                debug_s_things = cvdump.kaitai.coff.Coff.DebugS(size=section_header.size_of_raw_data, _io=kaitaistruct.KaitaiStream(io.BytesIO(section_raw_data)))
                print()
                print(f"    Signature: {debug_s_things.signature}")
                if hasattr(debug_s_things, "c13_stream"):
                    checksums = {}
                    for subsection in debug_s_things.c13_stream.subsections:
                        match subsection.header.type:
                            case C13LineStream.DebugSSubsectionType.debug_s_stringtable:
                                assert string_table is None
                                string_table = cvdump.names.StringTable.from_bytes(subsection.contents.data)
                            case C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                                assert not checksums
                                for cksum in subsection.contents.checksums:
                                    checksums[cksum.pos] = cksum
                    assert string_table is not None
                    assert checksums
                    for subsection in debug_s_things.c13_stream.subsections:
                        match subsection.header.type:
                            case C13LineStream.DebugSSubsectionType.debug_s_stringtable | C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                                break
                            case C13LineStream.DebugSSubsectionType.debug_s_symbols:
                                print("** SYMBOLS")
                                for symbol in subsection.contents.entries:
                                    cvdump.dump_symbol.dump_symbol(symbol=symbol, module_info=None, machine_config=machine_config)
                            case C13LineStream.DebugSSubsectionType.debug_s_framedata:
                                cvdump.dump_c13.dump_framedatas(subsection.contents)
                            case C13LineStream.DebugSSubsectionType.debug_s_lines:
                                print("** LINES")
                                cvdump.dump_c13.dump_lines(subsection.contents, string_table=string_table, checksums=checksums)
                            case _:
                                raise ValueError(subsection.header.type, subsection.header.type.name.upper())

                else:
                    raise ValueError(f"Unsupported .debug$S (signature=0x{debug_s_things.signature}:x)")
            elif section_header.name == b".debug$T":
                coff_file.seek(section_header.pointer_to_raw_data)
                debug_t_data = coff_file.read(section_header.size_of_raw_data)
                debug_t_signature, = struct.unpack_from("<I", debug_t_data)
                if debug_t_signature == 4:
                    bs = io.BytesIO(debug_t_data)
                    bs.seek(4)
                    tpi_records = cvdump.kaitai.tpi_stream.TpiStream.Records(kaitaistruct.KaitaiStream(bs))
                    cvdump.dump_tpi.dump_type_stream(tpi_records=tpi_records.records, ti_min=0, names_stream=string_table)
                else:
                    raise ValueError(f"Unsupported .debug$T signature: 0x{debug_t_signature:X}")
            elif section_header.name == b".text\x00\x00\x00" and section_header.characteristics & CODE_CHARACTERISTICS == CODE_CHARACTERISTICS:
                coff_file.seek(section_header.pointer_to_raw_data)
                text_data = coff_file.read(section_header.size_of_raw_data)

                cs_arch, cs_mode = machine_to_capstone_arch(cvdump.machine.Machine(coff.header.machine))
                md = capstone.Cs(cs_arch, cs_mode)

                for insn in md.disasm(text_data, 0x0):
                    # insn: capstone.CsInsn
                    print(f"0x{insn.address:08x}:\t{insn.mnemonic}\t{insn.op_str}")
            else:
                raise ValueError

    if string_table is not None:
        print()
        print("String table:")
        for k, v in string_table.offset_to_name.items():
            print(f"{k:4}: {v}")

if __name__ == "__main__":
    raise SystemExit(main())
