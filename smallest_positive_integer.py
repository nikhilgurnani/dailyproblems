"""
You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

[3, 4, -1, 1]
[4, 3, 1, -1]

[3, 4, -1, 2, 5]
[5, 4, 3, 2, -1]
"""

def first_missing_positive(nums):
    nums.sort(reverse=True)
    min_val = nums[0]
    for i in range(0, len(nums)):
        for j in range( i, len(nums) ):
            new_min = nums[i] - nums[j]
            if new_min > 0 and min_val > new_min and new_min not in nums:
                min_val = new_min
    return min_val

print(first_missing_positive([3, 4, -1, 1]))
# 2
print(first_missing_positive([3, 4, -1, 2, 5]))