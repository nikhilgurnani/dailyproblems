"""
Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4
"""

def jump(arr):

    i = 0
    max_jump = 0
    max_i = 0
    count = 0

    last_i = len(arr) - 1

    while last_i > 0:
        for j in range(i+1, arr[i] + i):
            if arr[j] <= last_i:
                last_i -= arr[j]
                i = j
                count += 1

    return count

print(jump([3, 2, 5, 1, 1, 9, 3, 4]))
print(jump([2,3,1,1,4]))
