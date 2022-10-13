# PEP 8
# https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator

# 1
def merge_the_tools(string, k):
    length = len(string)
    lenk = int(length / k)
    i = 1
    while i != lenk + 1:
        res = str()
        substring = string[(i-1)*k : k*i]
        for j in substring:
          if res.count(j) == 0:
            res += j      
        i += 1
    return


string = "ZXCZZXCXXABCCCC"
k = 3
merge_the_tools(string, k)


# 2
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    l = len(nums1)
    if l % 2 == 0:
        median = (nums1[l//2 - 1] + nums1[l//2]) / 2
    else:
        median = nums1[l//2]
    return median    


nums1 = [1, 4, 8]
nums2 = [2, 3]
findMedianSortedArrays(nums1, nums2)


# 3
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
    else:
        return 0


print(reverse(100))


# 4
def maxArea(height):
    length = len(height)
    maxS = 0
    for i in range(1, length):
        tmp1 = height[i-1]
        for j in range(i+1, length+1):
            tmp2 = height[j-1]
            y = min(tmp1, tmp2)
            x = j - i
            S = x * y
            if maxS < S:
                maxS = S
    return maxS


height = [5, 1, 5, 6]
maxArea(height)


# 5
def countDigitOne(n):
    sum = 0
    for i in range(1, n+1):
        tmp = i
        while tmp > 0:
            if tmp % 10 == 1:
                sum += 1
            tmp //= 10
    return sum


countDigitOne(13)
