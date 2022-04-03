from typing import List


def binary_search(array: List[int], target: int) -> int:
    ng, ok = -1, len(array)
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if target <= array[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def test_binary_search() -> None:
    array = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = 6
    expected = binary_search(array, 7)
    assert actual == expected
