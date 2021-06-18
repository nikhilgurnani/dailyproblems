"""
Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

Example:

Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)

Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.


[1, 2, 3, 7, 9, 5, 4, 3, 9, 10, 11]
"""

def findRange(nums):
    stack = [0] * len(nums)
    tos = -1
    i = 0
    while i < len(nums):
        if tos == -1 or nums[i] >= stack[tos]:
            tos += 1
            stack[tos] = nums[i]
            i += 1
        elif nums[i] < stack[tos]:
            break
    start = i - 1
    while i < len(nums):
        if nums[i] >= stack[tos]:
            break
        i += 1
    end = i - 1

    return start, end

print(findRange([1, 7, 9, 5, 7, 8, 10]))
print(findRange([1, 2, 3, 7, 9, 5, 4, 3, 9, 10, 11]))