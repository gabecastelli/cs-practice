class Node(object):
    def __init__(self, data, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

    def get_data(self):
        return self._data

    def set_data(self, data) -> None:
        self._data = data

    def get_prev(self):
        return self._prev

    def set_prev(self, prev) -> None:
        self._prev = prev

    def get_next(self):
        return self._next

    def set_next(self, next) -> None:
        self._next = next

    def __str__(self) -> str:
        return str(self._data)