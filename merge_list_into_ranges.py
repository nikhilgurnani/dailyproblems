"""
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.

Start at i = 1
At each i, check difference between  a[i] and a[i-1]
If difference is greater than 1, means that the next element cannot be a part of the current range. Push the current range to a list and set current range to current element, resetting the current range
If not, append the integer to current range
"""


def findRanges(nums):
    length = 1
    ranges = list()
    n = len(nums)

    for i in range(1, n+1):
        if  (i == n) or (nums[i] - nums[i-1] > 1):
            print(i, length, i-length)
            if length == 1:
                ranges.append(str(nums[i-length]) + '->' + str(nums[i-length]))
            else:
                ranges.append(str(nums[i-length]) + '->' + str(nums[i-1]))
                length = 1
        else:
            length += 1
    return ranges



# print(findRanges([0, 1, 2, 5, 6, 7]))
print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
