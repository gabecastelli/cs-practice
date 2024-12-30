from typing import Self, Any, Optional

class Node:
    def __init__(self, key, val):
        self._key = key
        self._val = val
        self._next = None

    def get_key(self) -> int:
        return self._key

    def get_val(self) -> Any:
        return self._val

    def get_next(self) -> Self:
        return self._next

    def set_next(self, next: Self) -> None:
        self._next = next


class HashTable:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._table = [None] * capacity

    def __hash(self, key) -> int:
        return hash(key) % self._capacity

    def __str__(self):
        arr = []

        for i in range(self._capacity):
            node_current = self._table[i]
            while node_current:
                arr.append((node_current.get_key(), node_current.get_val()))
                node_current = node_current.get_next()

        return str(arr)

    def insert(self, key, val) -> None:
        index = self.__hash(key)

        if self._table[index] is None:
            # Bucket is empty, insert new Node and increase size
            self._table[index] = Node(key, val)
            self._size += 1
        else:
            node_current = self._table[index]

            while node_current:
                if node_current.get_key() == key:
                    # Key exists, update its value
                    node_current.set_val(val)
                    return

                node_current = node_current.get_next()
            # Reached tail node of bucket, no match
            # Prepend new node and set it as head of the bucket
            node_new = Node(key, val)
            node_new.set_next(self._table[index])
            self._table[index] = node_new
            self._size += 1

    def search(self, key) -> Optional[Any]:
        index = self.__hash(key)
        node_current = self._table[index]

        while node_current:
            if node_current.get_key() == key:
                return node_current.get_val()

            node_current = node_current.get_next()

        return None

    def remove(self, key) -> None:
        index = self.__hash(key)
        node_previous = None
        node_current = self._table[index]

        while node_current:
            if node_current.get_key() == key:
                # Remove node from chain
                if node_previous:
                    node_previous.set_next(node_current.get_next())
                else:
                    self._table[index] = node_current.get_next()
                self._size -= 1
                return

            node_previous = node_current
            node_current = node_current.get_next()

        raise KeyError(key)


