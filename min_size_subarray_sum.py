"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Solution: https://leetcode.com/problems/minimum-size-subarray-sum/solution/
"""
import sys
class Solution:
    def minSubArrayLen(self, nums, s):
        min_length = sys.maxsize

        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= s:
                    min_length = min_length if min_length < ( j - i + 1 ) else (j - i + 1)
                    break
        return min_length if min_length < sys.maxsize else 0




print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2