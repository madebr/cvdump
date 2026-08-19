import struct

def pdb_hash_bytes_index(data: bytes, modulus: int) -> int:
    h = 0
    for i in range(len(data) // 4):
        h ^= struct.unpack_from("<I", data, offset=4*i)[0]
    if len(data) & 0x2:
        h ^= struct.unpack_from("<H", data, offset=len(data) & ~0x3)[0]
    if len(data) & 0x1:
        h ^= struct.unpack_from("<B", data, offset=len(data) & ~0x1)[0]
    h |= 0x20202020
    h ^= (h >> 11)
    h ^= (h >> 16)
    return h % modulus

def hash_string_long(text: bytes) -> int:
    return pdb_hash_bytes_index(text, 0xffffffff)

def hash_string_short(text: bytes) -> int:
    return pdb_hash_bytes_index(text, 0xffffffff) & 0xffff
