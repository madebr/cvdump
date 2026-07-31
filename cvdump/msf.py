# Parse Microsoft's Multi-stream format (wrapper for PDB files)
# https://llvm.org/docs/PDB/MsfFile.html

import io
import os
import typing

import kaitaistruct

from cvdump.kaitai.msf_small_superblock import MsfSmallSuperblock
from cvdump.kaitai.msf_small_directory import MsfSmallDirectory


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
    """ The tpi (type information) stream is always at index 2"""
    TPI_STREAM_INDEX = 2

    """ The dbi (debug information) stream is always at index 3"""
    DBI_STREAM_INDEX = 3

    def __init__(self, stream: typing.IO, superblock: MsfSmallSuperblock, directory: MsfSmallDirectory):
        self.stream = stream
        self.superblock = superblock
        self.directory = directory
        self.stream_block_maps: list[list[int]] = []

        stream_block_start = 0
        for stream_size in directory.stream_sizes:
            count_blocks = (stream_size.size + superblock.block_size - 1) // superblock.block_size
            stream_block_map = directory.stream_blocks[stream_block_start:stream_block_start+count_blocks]
            self.stream_block_maps.append(stream_block_map)
            stream_block_start += count_blocks

    @property
    def count_streams(self) -> int:
        return len(self.stream_block_maps)

    @classmethod
    def create(cls, stream: typing.IO[bytes]) -> "MsfFile":
        with kaitaistruct.KaitaiStream(stream) as kaitai_stream:
            superblock = MsfSmallSuperblock(kaitai_stream)
            # HACK: block kaitai from closing the bytes stream
            kaitai_stream._io = io.BytesIO()
        dir_msf_stream = MsfStream(stream, size=superblock.num_directory_bytes, block_size=superblock.block_size, block_map=superblock.block_map)
        with kaitaistruct.KaitaiStream(dir_msf_stream) as kaitai_stream:
            directory = MsfSmallDirectory(kaitai_stream)
            # HACK: block kaitai from closing the bytes stream
            kaitai_stream._io = io.BytesIO()
        return MsfFile(stream=stream, superblock=superblock, directory=directory)

    def create_stream(self, index: int) -> MsfStream:
        return MsfStream(stream=self.stream, size=self.directory.stream_sizes[index].size, block_size=self.superblock.block_size, block_map=self.stream_block_maps[index])
