# PEP 8
# https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator

# 1
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    length = len(string)
    len_k = int(length / k)
    i = 1
    while i != len_k + 1:
        res = str()
        substring = string[(i-1)*k : k*i]
        for j in substring:
          if res.count(j) == 0:
            res += j      
        i += 1
    return


# 2
# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
def find_median_sorted_arrays(nums1, nums2):
      union_array = nums1 + nums2
      union_array.sort()
      l = len(union_array)
      if l % 2 == 0:
          return (union_array[l//2-1] + union_array[l//2]) / 2
      return union_array[l//2]

# Or 
def _find_median_sorted_arrays(nums1, nums2):
    union_array = nums1 + nums2
    union_array.sort()
    l = len(union_array)
    match l % 2: 
        case 0:
            return (union_array[l//2-1] + union_array[l//2]) / 2
        case _:
          return union_array[l//2]  


# 3
# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
def reverse(x):
    tmp = abs(x)
    y = tmp % 10  
    tmp //= 10

    while tmp > 0:
        y *= 10
        y = y + (tmp % 10)
        tmp //= 10

    if x < 0:
        y =- y

    if y >= -2**31 and y <= 2**31 - 1:   
        return y
    return 0


# 4
# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
def max_area(height):
    length = len(height)
    max_s = 0
    for i in range(1, length):
        tmp1 = height[i-1]
        for j in range(i+1, length+1):
            tmp2 = height[j-1]
            y = min(tmp1, tmp2)
            x = j - i
            S = x * y
            if max_s < S:
                max_s = S
    return max_s


# 5
# Number of Digit One
# https://leetcode.com/problems/number-of-digit-one/
def count_digit_one(n):
    sum = 0
    for i in range(1, n+1):
        tmp = i
        while tmp > 0:
            if tmp % 10 == 1:
                sum += 1
            tmp //= 10
    return sum
