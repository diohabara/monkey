from operator import index
from random import shuffle
from typing import List


# sort [left, right)
def mergesort(array: List[int]) -> None:
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    mergesort(left)
    mergesort(right)
    l, r, current = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[current] = left[l]
            current += 1
            l += 1
        else:
            array[current] = right[r]
            current += 1
            r += 1
    while l < len(left):
        array[current] = left[l]
        current += 1
        l += 1
    while r < len(right):
        array[current] = right[r]
        current += 1
        r += 1


def test_mergesort() -> None:
    expected = [1, 2, 3, 3, 4, 5, 6]
    actual = expected[:]
    shuffle(actual)
    mergesort(actual)
    assert expected == actual
