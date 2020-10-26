"""
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, 4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

[ 5, 6, 8, -4, -9, 0, 1 ]

[ -9, -4, 0, 1, 5, 6, 8 ]

https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
"""
import math

def maximum_product_of_three(lst):

    length = len(lst)

    if len(lst) < 3:
        return max(0, math.prod( lst ))

    lst.sort()

    return max( (lst[length-1] * lst[length-2] * lst[length-3]), (lst[0] * lst[1] * lst[length-1] ))


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
print(maximum_product_of_three([ 5, 6, 8, -4, -9, 0, 1 ]))
# 288
