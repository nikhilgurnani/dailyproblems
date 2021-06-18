"""
You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

Help: https://leetcode.com/problems/product-of-array-except-self/solution/

**Explanation**
First, we iterate over the array and set the ouput array, such that output[i] contains product of elements upto nums[i-1]. So output[len(output)-1], would contain product up to len(nums)-1 elements from nums.

Then, for each product in that output, we need to multiple the elements from the Right side of Nums. We do that, by using a variable R which contains the product of elements in reverse from len(nums)-1.
"""

def products(nums):
    product = 1
    output = [1]*len(nums)

    for i in range(1, len(nums)):
        output[i] = output[i-1] * nums[i-1]

    R = 1
    for i in reversed(range(len(nums))):
        output[i] *= R
        R *= nums[i]

    return output
print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]