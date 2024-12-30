from typing import Self, Any

class Node:
    def __init__(self, val: Any=None, next: Self=None):
        self._val = val
        self._next = next

    def __str__(self):
        return str(self._val)

    def get_next(self) -> Self:
        return self._next

    def set_next(self, next: Self) -> None:
        self._next = next

    def get_data(self) -> Any:
        return self._val
