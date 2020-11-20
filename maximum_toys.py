def maximumToys(prices, k):
    prices.sort()
    count = 0
    print(prices)
    while k > 0:
        count += 1
        k = k - prices[count]
    return count

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
print(maximumToys([3, 7, 2, 9, 4], 15))
print(maximumToys([1, 2, 3, 4], 7))