"""
You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""

def room_schedulling(intervals):
    rooms = 0

    intervals = sorted(intervals)

    for i in range(1, len(intervals)+1):
        start_time = intervals[i][0]
        end_time = intervals[i][1]

        if start_time < intervals[i-1][1]:
            rooms += 1
        else:

    print(rooms)


room_schedulling([(30, 75), (0, 50), (60, 150)])