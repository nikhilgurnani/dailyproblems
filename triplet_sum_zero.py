"""
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

arr = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0

-3, -1, 0, 1, 2


"""

def findTriplets(arr):

    triplets = list()

    for i in range(0, len(arr)):
        items = set()
        for j in range(i+1, len(arr)):
            delta = -(arr[i] + arr[j])
            if delta in items:
                triplets.append([delta, arr[i], arr[j]])
            else:
                # add arr[j] because arr[i] is fixed element in the iterations, delta is calculated so the remaining is only arr[j]
                items.add(arr[j])
    return triplets

def findTripletsAlt(arr):
    arr = sorted(arr)
    triplets = list()

    i = 0
    r = len(arr) - 1

    for i in range(0, len(arr)):
        l = i + 1
        r = len(arr) - 1

        while l < r:
            delta = arr[i] + arr[l] + arr[r]
            if delta == 0:
                triplets.append([arr[i], arr[l], arr[r]])
                break
            elif delta < 0:
                l = l + 1
            else:
                r = r - 1
    return triplets
print(findTriplets([1, -2, 1, 0, 5]))
print(findTripletsAlt([0, -1, 2, -3, 1]))