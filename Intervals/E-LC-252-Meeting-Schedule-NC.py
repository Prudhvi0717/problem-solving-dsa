## link: https://neetcode.io/problems/meeting-schedule
## link: https://leetcode.com/problems/meeting-rooms/description/

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    Sort the intervals according to the start value.
    Now keep prev pointer to first interval and start iterating from 1 to len - 1 index.
    if prevEnd > curStart, then there is an overlap.
    return False.
    if not then update prevEnd to curEnd.

    """
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda i : i.start)

        prevEnd = intervals[0].end

        for cur in intervals[1:]:
            if prevEnd > cur.start:
                return False
            prevEnd = cur.end
        return True