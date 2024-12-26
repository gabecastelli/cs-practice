class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, val: int) -> None:
        self._queue.append(val)

    def dequeue(self) -> int:
        return self._queue.pop(0)

    def empty(self) -> bool:
        return not self._queue

    def __str__(self) -> str:
        return str(self._queue)