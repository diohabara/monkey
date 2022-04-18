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
    left_p, right_p, current = 0, 0, 0
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            array[current] = left[left_p]
            current += 1
            left_p += 1
        else:
            array[current] = right[right_p]
            current += 1
            right_p += 1
    while left_p < len(left):
        array[current] = left[left_p]
        current += 1
        left_p += 1
    while right_p < len(right):
        array[current] = right[right_p]
        current += 1
        right_p += 1


def test_mergesort() -> None:
    expected = [1, 2, 3, 3, 4, 5, 6]
    actual = expected[:]
    shuffle(actual)
    mergesort(actual)
    assert expected == actual
