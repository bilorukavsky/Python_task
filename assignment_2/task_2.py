# Remove Element
# https://leetcode.com/problems/remove-element/

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    number_of_val = nums.count(val)
    
    for _ in range(0, number_of_val):
        nums.remove(val)
        
    return len(nums)


def remove_element_one(nums: List[int], val: int) -> int:
    return len([i for i in nums if i != val])
