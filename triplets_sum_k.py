"""
Find triplets in an array whose sum is equal to K


a + b + c = K

[3, 4, 1, 6, 10, 0], K = 14
{10, 4, 0}
{10, 3, 1}

[0, 1, 3, 4, 6, 10]
 0, 1, 2, 3, 4, 5

for i = 0 to N (size of the array)
    j = i + 1
    r = n - 1

"""

def findTriplets(arr, k):
    arr = sorted(arr)

    triplets = list()

    for i in range(0, len(arr)):
        j = i + 1
        r = len(arr) - 1

        while j < r:
            sum = arr[i] + arr[j] + arr[r]
            if sum < k:
                j += 1
            elif sum > k:
                r -= 1
            else:
                triplets.append([arr[i], arr[j], arr[r]])
                break
    return triplets

def findTripletsAlt(arr, k):

    triplets = list()

    for i in range(0, len(arr)):
        items = set()
        for j in range(i+1, len(arr)):
            delta = k - arr[i] - arr[j]
            if delta in items:
                triplets.append([arr[i], arr[j], delta])
            else:
                items.add(arr[j])

    return triplets


print(findTriplets([0, 1, 3, 4, 6, 10], 14))
print(findTripletsAlt([0, 1, 3, 4, 6, 10], 14))