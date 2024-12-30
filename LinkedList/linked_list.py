from node import Node

class LinkedList(object):
    def __init__(self, head=None):
        self._head = head

    def __str__(self) -> str:
        if not self._head:
            return '[]'
        string = f'[{str(self._head)}'
        node_current = self._head
        while node_current.get_next():
            string += f' -> {str(node_current.get_next())}'
            node_current = node_current.get_next()
        return string + ']'

    def __set_head(self, head) -> None:
        self._head = head

    def get_head(self) -> Node:
        return self._head

    def find(self, value) -> int:
        if not self._head:
            return -1
        n = 0
        node_current = self._head
        while node_current:
            if node_current.get_data() == value:
                return n
            node_current = node_current.get_next()
            n += 1
        return -1

    def prepend(self, value) -> None:
        head_new = Node(value)
        head_new.set_next(self._head)
        head_new.get_next().set_prev(head_new)
        self._head = head_new

    def append(self, value) -> None:
        node_new = Node(value)
        if not self._head:
            self.__set_head(node_new)
            return
        node_current = self._head
        while node_current.get_next():
            node_current = node_current.get_next()
        node_current.set_next(node_new)
        node_current.get_next().set_prev(node_current)

    def pop_front(self):
        if not self._head:
            raise IndexError('Cannot pop front from empty list')
        self._head = self._head.get_next()
        if self._head:
            self._head.set_prev(None)

    def pop_back(self):
        if not self._head:
            raise IndexError('Cannot pop back from empty list')
        if not self._head.get_next():
            self._head = None
            return
        node_current = self._head
        while node_current.get_next():
            node_current = node_current.get_next()

        if node_current.get_prev():
            node_current.get_prev().set_next(None)
        node_current.set_prev(None)


    def insert(self, index, value) -> None:
        if index == 0:
            self.prepend(value)
            return
        n = 0
        node_current = self._head
        while node_current:
            if n == index - 1:
                node_new = Node(value)
                if node_current.get_next():
                    node_new.set_next(node_current.get_next())
                    node_new.get_next().set_prev(node_new)
                node_new.set_prev(node_current)
                node_current.set_next(node_new)
                return

            node_current = node_current.get_next()
            n += 1
        raise IndexError('Index out of bounds')

    def remove(self, index):
        if not self._head:
            raise IndexError('Cannot remove from empty list')
        if index == 0:
            self.pop_front()
        n = 0
        node_current = self._head
        while node_current:
            if n == index:
                if node_current.get_prev():
                    node_current.get_prev().set_next(node_current.get_next())
                if node_current.get_next():
                    node_current.get_next().set_prev(node_current.get_prev())
                return
            node_current = node_current.get_next()
            n += 1
        raise IndexError('Index out of bounds')
