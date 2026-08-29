class StringTable:
    def __init__(self, index_to_name: dict[int, str], offset_to_name: dict[int, str]):
        self._index_to_name = index_to_name
        self._offset_to_name = offset_to_name

    @classmethod
    def from_bytes(cls, data: bytes):
        index_to_name: dict[int, str] = {}
        offset_to_name: dict[int, str] = {}
        string_start = 0
        i = 0
        while string_start is not None:
            string_end = data.find(0, string_start)
            if string_end == -1:
                text = data[string_start:]
                next_string_start = None
            else:
                text = data[string_start:string_end]
                next_string_start = string_end + 1
            text = text.decode()
            index_to_name[i] = text
            offset_to_name[string_start] = text
            string_start = next_string_start
            i += 1
        return cls(index_to_name, offset_to_name)

    @classmethod
    def from_str(cls, data: str):
        index_to_name: dict[int, str] = {}
        offset_to_name: dict[int, str] = {}
        string_start = 0
        i = 0
        while string_start is not None:
            string_end = data.find("b\x00", string_start)
            if string_end == -1:
                text = data[string_start:]
                next_string_start = None
            else:
                text = data[string_start:string_end]
                next_string_start = string_end + 1
            index_to_name[i] = text
            offset_to_name[string_start] = text
            string_start = next_string_start
            i += 1
        return cls(index_to_name, offset_to_name)

    @property
    def offset_to_name(self) -> dict[int, str]:
        return self._offset_to_name

    def get_text_at_index(self, index: int) -> str:
        return self._index_to_name[index]

    def get_text_at_offset(self, offset: int) -> str:
        return self._offset_to_name[offset]
