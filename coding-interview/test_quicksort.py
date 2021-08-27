from typing import List


def quicksort(array: List[int]) -> List[int]:
    """
    Time: O(n log n)
    Space: O(n)
    """
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def test_quicksort() -> None:
    normal_array = [3, 6, 8, 10, 1, 2, 1]
    expected_normal = [1, 1, 2, 3, 6, 8, 10]
    assert quicksort(normal_array) == expected_normal
    duplicate_array = [7, 3, 3, 3, 4, 5]
    expected_duplicate = [3, 3, 3, 4, 5, 7]
    assert quicksort(duplicate_array) == expected_duplicate
    empty_array: List[int] = []
    assert quicksort(empty_array) == []
    reversed_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_reversed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quicksort(reversed_array) == expected_reversed
    single_element_array = [1]
    assert quicksort(single_element_array) == [1]
    all_the_same_array = [1, 1, 1, 1, 1, 1]
    assert quicksort(all_the_same_array) == [1, 1, 1, 1, 1, 1]


def partition(array: List[int], left_index: int, right_index: int) -> int:
    pivot = array[right_index]  # pivot is the last element
    greater_index = left_index  # pointer for the greater element than pivot
    for current_index in range(left_index, right_index):
        # if the current element is less than pivot, move it to the left
        if array[current_index] <= pivot:
            array[greater_index], array[current_index] = (
                array[current_index],
                array[greater_index],
            )
            greater_index += 1
    # swap greater element with pivot
    array[right_index], array[greater_index] = (
        array[greater_index],
        array[right_index],
    )
    return greater_index


def space_efficient_quicksort(
    array: List[int], left_index: int, right_index: int
) -> None:
    """
    Time: O(n log n)
    Space: O(log n)
    """
    if left_index < right_index:
        pivot = partition(array, left_index, right_index)
        space_efficient_quicksort(array, left_index, pivot - 1)
        space_efficient_quicksort(array, pivot + 1, right_index)


def test_space_efficient_quicksort() -> None:
    normal_array = [3, 6, 8, 10, 1, 2, 1]
    expected_normal = [1, 1, 2, 3, 6, 8, 10]
    space_efficient_quicksort(normal_array, 0, len(normal_array) - 1)
    assert normal_array == expected_normal
    duplicate_array = [7, 3, 3, 3, 4, 5]
    expected_duplicate = [3, 3, 3, 4, 5, 7]
    space_efficient_quicksort(duplicate_array, 0, len(duplicate_array) - 1)
    assert duplicate_array == expected_duplicate
    empty_array: List[int] = []
    space_efficient_quicksort(empty_array, 0, len(empty_array) - 1)
    assert empty_array == []
    reversed_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_reversed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    space_efficient_quicksort(reversed_array, 0, len(reversed_array) - 1)
    assert reversed_array == expected_reversed
    single_element_array = [1]
    space_efficient_quicksort(single_element_array, 0, len(single_element_array) - 1)
    assert single_element_array == [1]
    all_the_same_array = [1, 1, 1, 1, 1, 1]
    space_efficient_quicksort(all_the_same_array, 0, len(all_the_same_array) - 1)
    assert all_the_same_array == [1, 1, 1, 1, 1, 1]
