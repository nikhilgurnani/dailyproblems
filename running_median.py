"""
You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

Odd Items:
(n+1/2)th term => If n = 3, median = (3+1)/2 => 4/2 => 2nd Term

Even Items:
((n/2)th + ((n/2) + 1)th) / 2 => If n = 4, median = (2nd + 3rd) / 2
"""

def running_median(stream):
    median = [0] * len(stream)
    median[0] = stream[0]

    for i in range(1, len(stream)):
        n = i+1
        if (n % 2 == 0):
            median_index_first = (n) // 2
            median_index_second = (n//2) + 1
            print(i,median_index_first, median_index_second)
            median[i] = (stream[median_index_first-1] + stream[median_index_second-1]) / 2
        else:
            median_index = (n+1)//2
            median[i] = stream[median_index-1]
    return median


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
