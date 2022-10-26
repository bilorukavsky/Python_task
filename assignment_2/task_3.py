# Single number
# https://leetcode.com/problems/single-number/

from typing import List


def single_number(nums: List[int]) -> int:
    for i in range(0, len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]


def single_number_one(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i


def single_number_two(nums: List[int]) -> int:
    [result] = [i for i in nums if nums.count(i) == 1]
    return result


def single_number_three(nums: List[int]) -> int:
    return [i for i in nums if nums.count(i) == 1][0]
