from typing import List


class Stack:
    def __init__(self) -> None:
        self._items: List[int] = []
        self._size = 0

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def top(self) -> int:
        if self._size == 0:
            raise Exception("No elements")
        return self._items[self._size - 1]

    def push(self, x: int) -> None:
        self._items.append(x)
        self._size += 1

    def pop(self) -> int:
        self._size -= 1
        return self._items.pop()


def test_stack() -> None:
    stack = Stack()
    assert stack.empty()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    expected0 = 3
    actual0 = stack.top()
    assert expected0 == actual0
    expected1 = 3
    actual1 = stack.pop()
    assert expected1 == actual1
    expected2 = 2
    actual2 = stack.top()
    assert expected2 == actual2
    expected3 = 2
    actual3 = stack.size()
    assert expected3 == actual3
