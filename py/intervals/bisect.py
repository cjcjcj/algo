"""
    [left; right)

    add/remove  O(logn + n)
    query       O(logn)

    Odd positions lie between ranges.
    Array always has an even # of elements.

    [8, 10] (7, 8)      -> track[0:1] = [7]      -> [7, 10]
    [8, 10] (10, 11)    -> track[1:2] = [11]     -> [8, 11]
    [8, 10] (0, 1)      -> track[0:0] = [0, 1]   -> [0, 1, 8, 10]
    [8, 10] (11, 12)    -> track[2:2] = [11, 12] -> [8, 10, 11, 12]
    [1, 4, 7, 9] (3,8)  -> track[1:3] = []       -> [1, 9]

    https://leetcode.com/problems/range-module
"""

import bisect


class Intervaler:
    def __init__(self):
        self.track = []
    def add(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def remove(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def query(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1
