"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


input = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

zero_index = [ 0, 1, 2, 4, 8, 9 ]

non_zero_index = [ 3, 5, 6, 7]

"""


class Solution:
    def moveZeros(self, nums):
        zero_indexes = []

        non_zero_indexes = []

        for index, value in enumerate( nums ):
            if value > 0:
                non_zero_indexes.append( index )

        index = 0
        for i in non_zero_indexes:
            temp = nums[ i ]
            nums[i] = nums[index]
            nums[index] = temp
            index += 1
    def moveZeroesAlt(self, nums):
        count = 0

        for index, value in enumerate( nums ):
            if value > 0:
                temp = nums[index]
                nums[index] = nums[count]
                nums[ count ] = temp
                count += 1


        while count > len(nums):
            count += 1
            nums[count] = 0



nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

nums = [ 0, 0, 1, 2, 3, 4, 0, 0 ]
Solution().moveZeroesAlt(nums)
print(nums)
