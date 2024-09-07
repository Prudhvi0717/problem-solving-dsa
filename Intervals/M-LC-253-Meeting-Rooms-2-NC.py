## link: https://leetcode.com/problems/meeting-rooms-ii/description/
## link: https://neetcode.io/problems/meeting-schedule-ii

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    The first idea is to create rooms array [[intervals]]
    where non overlapping intervals are stored in same room.

    Sort the intervals and initiate rooms arr as [[intervals[0]]]

    for each interval from 1 to len(intervals) - 1 index
    check each room if it could non overlappingly added to that room.
    if not at the end of loop create a new room to add this interval.
    return the len(rooms)
    
    -----

    Second solution is to sort start times arr and end time array.
    Take two pointers at each of start and end arrs.
    Take counter rooms = 0

    compare start ptr val and end ptr val
    if start is less increase the counter indicating a meeting started.
    if end is less derement the counter indicating a meeting ended.

    Track the max val of rooms counter indicating the max concurrent meetings.

    """
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals: return 0
        # intervals.sort(key = lambda i : i.start)

        # rooms = [[intervals[0]]]

        # for i in intervals[1:]:
        #     found = False
        #     for r in range(len(rooms)):
        #         if rooms[r][-1].end <= i.start:
        #             rooms[r].append(i)
        #             found = True
        #             break
        #     if not found: rooms.append([i])

        # return len(rooms)

        s, e, rooms, res = 0, 0, 0, 0
        start, end = [i.start for i in intervals], [i.end for i in intervals]
        start.sort()
        end.sort()
        

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            res = max(res, rooms)
        return res
        
