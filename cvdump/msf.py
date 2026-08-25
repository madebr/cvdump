# Parse Microsoft's Multi-stream format (wrapper for PDB files)
# https://llvm.org/docs/PDB/MsfFile.html

import io
import os
import typing

import kaitaistruct

from cvdump.kaitai.msf import Msf


class MsfStream:
    __slots__ = (
        "stream",
        "size",
        "pos",
        "block_size",
        "block_map",
        "block_data",
    )

    def __init__(self, stream: typing.IO, size: int, block_size: int, block_map: list[int]):
        self.stream = stream
        self.size = size
        self.pos = 0
        self.block_size = block_size
        self.block_map = block_map
        self.block_data: bytes = b""

    def _do_seek(self) -> None:
        if self.pos >= self.size:
            self.pos = self.size
            return

        block_idx = self.pos // self.block_size
        block = self.block_map[block_idx]
        self.stream.seek(block * self.block_size)

        read_size = self.block_size
        if block_idx == len(self.block_map) - 1 and self.size % self.block_size != 0:
            read_size = self.size % self.block_size

        self.block_data = self.stream.read(read_size)

    def read(self, size: int|None=None) -> bytes:
        if size is None or size == -1:
            size = self.size - self.pos
        elif size < 0:
            raise ValueError(size)
        elif size == 0:
            return b""
        else:
            size = min(self.size - self.pos, size)

        result_pos = 0
        result = bytearray(size)

        while result_pos < size:
            block_data_pos = self.pos % self.block_size
            if block_data_pos == 0:
                self._do_seek()

            assert len(self.block_data) > 0
            amount = min(size - result_pos, len(self.block_data) - block_data_pos)
            assert amount > 0
            result[result_pos:result_pos+amount] = self.block_data[block_data_pos:block_data_pos+amount]
            self.pos += amount
            result_pos += amount

        return bytes(result)

    def write(self, data: bytes, size: int=-1) -> None:
        raise io.UnsupportedOperation

    def seek(self, n, whence=os.SEEK_SET) -> None:
        oldpos = self.pos
        match whence:
            case os.SEEK_SET:
                self.pos = n
            case os.SEEK_CUR:
                self.pos += n
            case os.SEEK_END:
                self.pos = self.size + n
            case _:
                raise ValueError(whence)
        if oldpos != self.pos:
            self._do_seek()

    def close(self):
        pass

    def tell(self) -> int:
        return self.pos


class MsfFile:
    """ The pdb stream is always at index 1"""
    PDB_STREAM_INDEX = 1

    """ The tpi (type information) stream is always at index 2"""
    TPI_STREAM_INDEX = 2

    """ The dbi (debug information) stream is always at index 3"""
    DBI_STREAM_INDEX = 3

    """ The ipi stream is always at index 4"""
    IPI_STREAM_INDEX = 4

    LINK_INFO_STREAM_NAME = "/LinkInfo"
    HEADERBLOCK_STREAM_NAME = "/src/headerblock"
    NAMES_STREAM_NAME = "/names"

    def __init__(self, stream: typing.IO, block_size: int, stream_sizes: list[int], stream_blocks: list[int], msf: Msf):
        self.stream = stream
        self.block_size = block_size
        self.stream_block_maps: list[list[int]] = []
        self.stream_sizes = stream_sizes
        self.msf = msf

        stream_block_start = 0
        for stream_size in stream_sizes:
            count_blocks = (stream_size + block_size - 1) // block_size
            stream_block_map = stream_blocks[stream_block_start:stream_block_start+count_blocks]
            self.stream_block_maps.append(stream_block_map)
            stream_block_start += count_blocks

    @property
    def count_streams(self) -> int:
        return len(self.stream_block_maps)

    @classmethod
    def create(cls, stream: typing.IO[bytes]) -> "MsfFile":
        with kaitaistruct.KaitaiStream(stream) as kaitai_stream:
            msf = Msf(kaitai_stream)
            # HACK: block kaitai from closing the bytes stream
            kaitai_stream._io = io.BytesIO()
        if msf.is_small_msf and msf.small_msf_version != 2:
            raise ValueError(f"Small MSF stream version {msf.small_msf_version} not supported (yet)")
        if msf.is_big_msf:
            stream.seek(msf.big_superblock.block_map_address * msf.big_superblock.block_size)
            with kaitaistruct.KaitaiStream(stream) as kaitai_stream:
                count_directory_pages = (msf.big_superblock.num_directory_bytes + msf.big_superblock.block_size) // msf.big_superblock.block_size
                big_msf_dir_pages = Msf.BigMsfStreamDirectoryPages(_io=kaitai_stream, count_items=count_directory_pages)
                if len(big_msf_dir_pages.pages) != count_directory_pages:
                    raise ValueError(f"Expected {count_directory_pages} entries in directory, got {len(big_msf_dir_pages.pages)}")
                # HACK: block kaitai from closing the bytes stream
                kaitai_stream._io = io.BytesIO()
            stream.seek(0)
            with kaitaistruct.KaitaiStream(MsfStream(stream=stream, size=msf.big_superblock.num_directory_bytes, block_size=msf.big_superblock.block_size, block_map=big_msf_dir_pages.pages)) as kaitai_stream:
                big_msf_stream_directory = Msf.BigMsfStreamDirectory(kaitai_stream)
            stream_blocks = big_msf_stream_directory.stream_blocks
            stream_sizes = big_msf_stream_directory.stream_sizes
            block_size = msf.big_superblock.block_size
        else:
            with kaitaistruct.KaitaiStream(MsfStream(stream=stream, size=msf.small_superblock.num_directory_bytes, block_size=msf.small_superblock.block_size, block_map=msf.small_superblock.block_map)) as kaitai_stream:
                small_msf_stream_directory = Msf.SmallMsfStreamDirectory(kaitai_stream)
                # HACK: block kaitai from closing the bytes stream
                kaitai_stream._io = io.BytesIO()
            stream_sizes = [sz.size for sz in small_msf_stream_directory.stream_sizes]
            block_size = msf.small_superblock.block_size
            stream_blocks = small_msf_stream_directory.stream_blocks
        return MsfFile(stream=stream, block_size=block_size, stream_sizes=stream_sizes, stream_blocks=stream_blocks, msf=msf)

    def create_stream(self, index: int) -> MsfStream:
        return MsfStream(stream=self.stream, size=self.stream_sizes[index], block_size=self.block_size, block_map=self.stream_block_maps[index])
