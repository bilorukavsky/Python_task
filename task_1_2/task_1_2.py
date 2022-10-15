# Remove Element
# https://leetcode.com/problems/remove-element/
def remove_element(nums: list[int], val: int) -> int:
    number_of_val = nums.count(val)
    
    for i in range(0, number_of_val):
        nums.remove(val)
        
    return len(nums)



        
        
    
