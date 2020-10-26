"""
You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

Step 1: Sort the array based on X assuming the pairs are (x, y)

Step 2: Set max_x as 1, min_y as 3

Step 3: For each remaining pair in the intervals, check if both X and Y are greater than max_x and smaller than min_y respectively (to check if the value lies within the range)

Step 4: If it does, continue. If it doesn't, set max_x as X and min_y as Y

(1, 3)
(4, 10)
(5, 8)
(20, 25)
"""


def merge(intervals):

    intervals.sort()

    new_list = list()

    max_x, min_y = intervals[0]

    new_list.append((max_x, min_y))

    for index in range( 1, len(intervals)):
        if max_x <= intervals[index][0] <= min_y:
            if max_x <= intervals[index][1] <= min_y:
                continue
        max_x = intervals[index][0]
        min_y = intervals[index][1]
        new_list.append( intervals[index] )
    return new_list




print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]

print(merge([(1, 3), (5, 8), (4, 10), (20, 25), (6, 9), (21, 26)]))
# [(1, 3), (4, 10), (20, 25), (21, 26)]