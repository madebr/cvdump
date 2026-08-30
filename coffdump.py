#!/usr/bin/env python3

import argparse
import binascii
import datetime
import io
import pathlib
import struct
import textwrap

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
def relocation_type_to_str(t: int, machine: cvdump.machine.Machine) -> str:
    match machine:
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_I386:
            return cvdump.pe_coff.CoffRelocationI386(t).name
        case cvdump.machine.Machine.IMAGE_FILE_MACHINE_AMD64:
            return cvdump.pe_coff.CoffRelocationAMD64(t).name
        case _:
            raise NotImplementedError(machine, t)


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("coff", type=pathlib.Path)
    args = parser.parse_args()

    with args.coff.open("rb") as coff_file:
        coff = cvdump.kaitai.coff.Coff(kaitaistruct.KaitaiStream(coff_file))
        machine = cvdump.machine.Machine(coff.header.machine)

        print(f"                Machine: {machine.name}")
        print(f"     Number of sections: {coff.header.number_of_sections}")
        print(f"        Time date stamp: {datetime.datetime.fromtimestamp(coff.header.time_date_stamp).strftime('%Y-%m-%d %H:%M:%S')} (0x{coff.header.time_date_stamp:08x})")
        print(f"Pointer to Symbol Table: 0x{coff.header.pointer_to_symbol_table:08x}")
        print(f"      Number of symbols: {coff.header.number_of_symbols}")
        print(f"Size of optional header: 0x{coff.header.size_of_optional_header:04x}")
        print(f"        Characteristics: {cvdump.pe_coff.PeCoffCharacteristic(coff.header.characteristics)} (0x{coff.header.characteristics:04x})")

        for section_i, section_header in enumerate(coff.section_headers, 1):
            print()
            print(f"- Section {section_i}:")
            section_name = section_header.name.rstrip(b"\x00").decode("ascii")
            print(f"                    name: {section_name}")
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
            DATA_CHARACTERISTICS = cvdump.pe_coff.PeCoffSectionFlags.IMAGE_SCN_CNT_INITIALIZED_DATA
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
                if hasattr(debug_s_things, "symbols"):
                    # Visual Studio 4.2
                    assert debug_s_things.signature == 1
                    print("** SYMBOLS")
                    for symbol in debug_s_things.symbols.entries:
                        cvdump.dump_symbol.dump_symbol(symbol=symbol, module_info=None, machine_config=machine_config)
                elif hasattr(debug_s_things, "c13_stream"):
                    # Visual Studio 2012
                    assert debug_s_things.signature == 4
                    checksums = {}
                    names_table = None
                    for subsection in debug_s_things.c13_stream.subsections:
                        match subsection.header.type:
                            case C13LineStream.DebugSSubsectionType.debug_s_stringtable:
                                assert names_table is None
                                names_table = cvdump.names.StringTable.from_bytes(subsection.contents.data)
                            case C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                                assert not checksums
                                for cksum in subsection.contents.checksums:
                                    checksums[cksum.pos] = cksum
                    assert names_table is not None
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
                                cvdump.dump_c13.dump_lines(subsection.contents, string_table=names_table, checksums=checksums)
                            case _:
                                raise ValueError(subsection.header.type, subsection.header.type.name.upper())

                    if names_table is not None:
                        print()
                        print("Names table:")
                        for k, v in names_table.offset_to_name.items():
                            print(f"{k:4}: {v}")

                else:
                    raise ValueError(f"Unsupported .debug$S (signature=0x{debug_s_things.signature}:x)")
            elif section_header.name == b".debug$T":
                coff_file.seek(section_header.pointer_to_raw_data)
                debug_t_data = coff_file.read(section_header.size_of_raw_data)
                debug_t_signature, = struct.unpack_from("<I", debug_t_data)
                if debug_t_signature in (1, 4):
                    # 1: Visual Studio 4.2
                    # 4: Visual Studio 2012
                    bs = io.BytesIO(debug_t_data)
                    bs.seek(4)
                    tpi_records = cvdump.kaitai.tpi_stream.TpiStream.Records(kaitaistruct.KaitaiStream(bs))
                    cvdump.dump_tpi.dump_type_stream(tpi_records=tpi_records.records, ti_min=0, names_stream=None)
                else:
                    raise ValueError(f"Unsupported .debug$T signature: 0x{debug_t_signature:X}")
            elif section_header.name in (b".data\x00\x00\x00", b".rdata\x00\x00") and section_header.characteristics & DATA_CHARACTERISTICS == DATA_CHARACTERISTICS:
                coff_file.seek(section_header.pointer_to_raw_data)
                data = coff_file.read(section_header.size_of_raw_data)
                print(f"data = ", end="")
                print("\n   ".join(textwrap.wrap(binascii.b2a_hex(data).decode())))
            elif section_header.name == b".text\x00\x00\x00" and section_header.characteristics & CODE_CHARACTERISTICS == CODE_CHARACTERISTICS:
                coff_file.seek(section_header.pointer_to_raw_data)
                text_data = coff_file.read(section_header.size_of_raw_data)

                cs_arch, cs_mode = machine_to_capstone_arch(cvdump.machine.Machine(coff.header.machine))
                md = capstone.Cs(cs_arch, cs_mode)

                for insn in md.disasm(text_data, 0x0):
                    # insn: capstone.CsInsn
                    print(f"0x{insn.address:08x}:\t{insn.mnemonic}\t{insn.op_str}")
            else:
                raise ValueError(section_header.name)

            if section_header.pointer_to_relocations == 0:
                print(" Section does not contain relocations")
            else:
                coff_file.seek(section_header.pointer_to_relocations)
                relocation_data = coff_file.read(section_header.number_of_relocations * 0xa)
                relocations = cvdump.kaitai.coff.Coff.Relocations(kaitaistruct.KaitaiStream(io.BytesIO(relocation_data)))
                print(" Relocations:")
                for relocation in relocations.items:
                    print(f"- address: 0x{relocation.virtual_address:08x}, symbol={relocation.symbol_table_index:6}, type={relocation_type_to_str(relocation.type, machine=machine)}")

        coff_file.seek(coff.header.pointer_to_symbol_table + 0x12 * coff.header.number_of_symbols)
        string_table_bytes = coff_file.read()
        def get_name_from_string_table(offset: int) -> str:
            pos_end = string_table_bytes.find(0, offset)
            if pos_end == -1:
                name = string_table_bytes[offset:]
            else:
                name = string_table_bytes[offset:pos_end]
            return name.decode("ascii")
        
        def get_symbol_name(raw_name: bytes) -> str:
            magic, name_offset = struct.unpack("<II", raw_name)
            if magic == 0:
                name = get_name_from_string_table(offset=name_offset)
            else:
                raw_name = raw_name.rstrip(b"\x00")
                try:
                    name = raw_name.decode("ascii")
                except:
                    name = str(raw_name)
            return name

        coff_file.seek(coff.header.pointer_to_symbol_table)
        symbol_table_raw_table = coff_file.read(0x12 * coff.header.number_of_symbols)
        symbol_table = cvdump.kaitai.coff.Coff.SymbolTable(kaitaistruct.KaitaiStream(io.BytesIO(symbol_table_raw_table)))

        def get_section_number_name(v: int) -> str:
            match v:
                case 0: 
                    return "IMAGE_SYM_UNDEFINED"
                case -1:
                    return "IMAGE_SYM_ABSOLUTE"
                case -2:
                    return "IMAGE_SYM_DEBUG "
            return str(v)
            
        def get_symbol_type_representation(type_value: int) -> str:
            match type_value:
                case 0x00:
                    return "NOT_A_FUNCTION"
                case 0x20:
                    return "FUNCTION"
            try:
                base_type = type_value & 0xff
                complex_type = type_value >> 8
                base_name = cvdump.pe_coff.CoffSymbolBaseType(base_type).name
                complex_name = cvdump.pe_coff.CoffSymbolComplexType(complex_type).name
                return f"{base_name}/{complex_name}"
            except ValueError:
                return "???"
        def get_symbol_storage_class_description(v: int) -> str:
            try:
                return cvdump.pe_coff.CoffSymbolStorageClass(v).name
            except ValueError:
                return "???"

        print()
        print("** COFF Symbol table")
        print()
        def dump_symbol_table_item(symbol: cvdump.kaitai.coff.Coff.SymbolTableItem, symbol_index: int, depth: int):
            space = " "
            indent = 2 * depth
            name = get_symbol_name(symbol.name)
            print(f"{symbol_index:>{indent}} name: '{name}'")
            print(f"{space:>{indent}} value: 0x{symbol.value:08x}")
            print(f"{space:>{indent}} section: {get_section_number_name(symbol.section_number)} ({symbol.section_number})")
            print(f"{space:>{indent}} type: {get_symbol_type_representation(symbol.type)} (0x{symbol.type:04x})")
            print(f"{space:>{indent}} storage class: {get_symbol_storage_class_description(symbol.storage_class)} (0x{symbol.storage_class:02x})")
            print(f"{space:>{indent}} number of aux symbols: {symbol.number_of_aux_symbols}")
            return symbol_index + 1 + symbol.number_of_aux_symbols

        symbol_index = 0
        for symbol in symbol_table.items:
            symbol_index = dump_symbol_table_item(symbol, symbol_index=symbol_index, depth=2)

if __name__ == "__main__":
    raise SystemExit(main())
