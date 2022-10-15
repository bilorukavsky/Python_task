# Single number
# https://leetcode.com/problems/single-number/
def single_number(nums: list[int]) -> int:
    for i in range(0, len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]

        

    
    
