"""
You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
"""
import sys
def buy_and_sell(arr):
    min_price = sys.maxsize
    max_profit = 0

    for i in range(0, len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        max_profit = max( max_profit, (arr[i] - min_price))

    return max_profit

# O(n^2)
# def buy_and_sell(arr):
#     max_diff = -1
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             max_diff = max(arr[j] - arr[i], max_diff)

#     return max_diff

def buy_and_sell_alt(arr):
    copy = arr
    copy.sort()

    return copy[ len(copy) - 1 ] - copy[ 0 ]


print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
print(buy_and_sell([9, 11, 8, 5, 1, 10, 12, 14, 16, 20, 25, 6, 5, 10, 45]))
# 44
