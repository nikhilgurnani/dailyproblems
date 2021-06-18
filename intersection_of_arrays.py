"""
Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Help: https://www.geeksforgeeks.org/find-union-and-intersection-of-two-unsorted-arrays/
"""

class Solution:
    def binary_search(self, arr, key, start, end):
        if start > end:
            return False
        mid = (start + end) // 2
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            return self.binary_search(arr, key, start, mid-1)
        elif key > arr[mid]:
            return self.binary_search(arr, key, mid+1, end)

    def intersection_helper(self, small_nums, nums, intersection):
        for i in nums:
            if i in intersection:
                continue
            elif self.binary_search(small_nums, i, 0, len(small_nums)-1):
                intersection.add(i)

    def intersection(self, nums1, nums2):
        intersection = set()
        if len(nums1) <= len(nums2):
            nums1 = sorted(nums1)
            self.intersection_helper(nums1, nums2, intersection)
        else:
            nums2 = sorted(nums2)
            self.intersection_helper(nums2, nums1, intersection)
        return intersection


print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]