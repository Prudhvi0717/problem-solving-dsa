## link: https://leetcode.com/problems/insert-interval/

class Solution:
    """
    if current interval start > newInterval end, add the newInterval to res and rem intervals, return.
    if current interval end < start, then append the current interval to res and move on.
    If not both the above cases there is an overlap in the intervals so update the new interval,
    newInterval = [min(currentStart, newIntervalStart), max(currentEnd, newIntervalEnd)]
    This interval be added before any interval in the first if condition.
    If not we add it to res after the loop terminates.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval[0], newInterval[1]
        
        for i in range(len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                return res + intervals[i:]
            elif intervals[i][1] < start:
                res.append(intervals[i])
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])

        res.append([start, end])
        return res