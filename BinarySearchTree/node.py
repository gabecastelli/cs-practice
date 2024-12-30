from typing import Self

class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self._key = key
        self._left = left
        self._right = right

    @property
    def key(self):
        return self._key
    
    @property
    def left(self) -> Self:
        return self._left
    
    @property
    def right(self) -> Self:
        return self._right

    @staticmethod
    def insert(node: Self, key) -> Self:
        """Insert `key` recursively in the tree or subtree of `node`.
        Does not check for duplicates in the supertree.
        """
        if not node:
            node = Node(key)

        if node.key == key:
            raise ValueError(f'Duplicate key: key {key} already exists.')
        
        if node.key > key:
            node.right = Node.insert(node.right, key)
        else:
            node.left = Node.insert(node.left, key)

        return node
