from typing import List, Optional


class ksort:

    def __init__(self) -> None:
        self.items: List[Optional[str]] = [None] * 800
        self.ITEMS_OFFSET: dict[str, int] = {
            "a": 0,
            "b": 100,
            "c": 200,
            "d": 300,
            "e": 400,
            "f": 500,
            "g": 600,
            "h": 700,
        }

    def __is_string_valid(self, s: str) -> bool:
        return (
            len(s) == 3
            and s[0] in self.ITEMS_OFFSET
            and s[1] in [str(i) for i in range(10)]
            and s[2] in [str(i) for i in range(10)]
        )

    def index(self, s: str) -> int:
        if not self.__is_string_valid(s):
            return -1
        return self.ITEMS_OFFSET[s[0]] + int(s[1:])

    def add(self, s: str) -> bool:
        index_for_save: int = self.index(s)
        if index_for_save == -1:
            return False
        self.items[index_for_save] = s
        return True
