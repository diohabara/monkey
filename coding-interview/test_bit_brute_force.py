from typing import List


def bit_brute_force(nums: List[int], target: int) -> bool:
    size = len(nums)
    for mask in range(1 << size):
        current_sum = 0
        for i in range(size):
            if mask & 1 << i:
                current_sum += nums[i]
        if current_sum == target:
            return True
    return False


def test_bit_brute_force() -> None:
    nums1 = [2, 3, 5, 7, 11]
    target1 = 12
    assert bit_brute_force(nums1, target1)
