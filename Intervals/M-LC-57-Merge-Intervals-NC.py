## link: https://leetcode.com/problems/insert-interval/

class Solution:
    """
    Sort according to their starts. 
    And while merging just check if the second list start <= previous list end. 
    If yes set end = max(firstListEnd , secondListEnd) else the intervals are disjoint hence 
    simply add the current Interval without making any changes to the previous interval.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result
