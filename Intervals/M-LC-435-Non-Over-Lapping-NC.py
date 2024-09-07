## link : https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    """
    Sort the intervals according to the start value.
    Now keep prev pointer to first interval and start iterating from 1 to len - 1 index.

    Since the intervals are sorted, an overlap could be identified by
    prev[1] > cur[0]

    If true, then we need remove one of them, how do we decide ?
    We keep the interval which has lesser end value.
    i.e prev = prev if prev[1] <= cur[1] else cur
    and we increase the result counter.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0

        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1] > cur[0]:
                prev = prev if prev[1] <= cur[1] else cur
                res += 1
            else:
                prev = cur

            
        return res