from typing import Any
from node import Node

class Queue:
    def __init__(self, head: Any=None):
        self._head = Node(head)
        self._tail = self._head

    def __str__(self) -> str:
        if not self._head:
            return ''
        node_current = self._head.get_next()
        string = '[' + str(self._head)
        while node_current:
            string += f' -> {node_current}'
            node_current = node_current.get_next()
        return string + ']'

    def enqueue(self, val) -> None:
        node_new = Node(val)
        self._tail.set_next(node_new)
        self._tail = node_new

    def dequeue(self) -> Any:
        node_removed = self._head
        self._head = self._head.get_next()
        return node_removed.get_data()

    def empty(self) -> bool:
        return not self._head
