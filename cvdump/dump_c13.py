import binascii
import enum

from cvdump.kaitai.c13_line_stream import C13LineStream
from cvdump.names import StringTable


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


def dump_lines(debug_lines: C13LineStream.DebugLines, string_table: StringTable, checksums: dict[int, C13LineStream.Filechecksum]):
    for table_i, table in enumerate(debug_lines.tables.items):
        cksum = checksums[table.fileid]
        filename = string_table.get_text_at_offset(cksum.name_index)
        start = debug_lines.off_con if table_i == 0 else (debug_lines.off_con + table.lines[0].offset)
        end = (debug_lines.off_con + debug_lines.count_con) if table_i + 1 == len(
            debug_lines.tables.items) else (
                    debug_lines.off_con + debug_lines.tables.items[table_i + 1].lines[0].offset)
        print()
        print(
            f"  {filename} ({get_hash_name(cksum.hash_type)}: {binascii.b2a_hex(cksum.hash).decode().upper()}), {debug_lines.seg_con:04X}:{start:08X}-{end:08X}, line/addr pairs = {table.count_lines}")
        print()
        for i, line_item in enumerate(table.lines):
            if line_item.line_number_start in (0xfeefee, 0xf00f00):
                print(f"  {line_item.line_number_start:x} {debug_lines.off_con + line_item.offset:08X}", end="")
            else:
                print(f"  {line_item.line_number_start:5} {debug_lines.off_con + line_item.offset:08X}", end="")
            if i % 4 == 3 or i == len(table.lines) - 1:
                print()


def dump_framedatas(framedatas: C13LineStream.Framedatas):
    # print(f"RVACon = {framedatas.rva_con:08x}")
    print(f" Address  Blk Size   cbLocals cbParams cbStkMax cbProlog  cbSavedRegs SEH C++EH FStart  Program")
    for frame in framedatas.frames:
        print(f"{frame.rva_start:08X}  {frame.size_block:8X}   {frame.size_locals:8X} {frame.size_params:8X} {frame.size_stack_max:8X} {frame.size_prolog:8X}     {frame.size_saved_regs:8X}   {'Y' if frame.flags & 0x1 else 'N'}     {'Y' if frame.flags & 0x2 else 'N'}      {'Y' if frame.flags & 0x4 else 'N'} {frame.frame_func:08X}")
