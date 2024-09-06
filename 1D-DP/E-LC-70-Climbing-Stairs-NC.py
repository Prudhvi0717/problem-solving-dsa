## link: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    """
    To find how many distinct ways we could reach the top.
    So we use bottom up approach, we start from top and reach the start.
    """
    def climbStairs(self, n: int) -> int:
        # cache = {0 : 0, 1 : 1, 2 : 2}

        # def getWaysFrom(n):
        #     if n in cache: return cache[n]
        #     if n < 0: return 0

        #     cache[n] = getWaysFrom(n - 1) + getWaysFrom(n - 2)
        #     return cache[n]

        # return getWaysFrom(n)

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
            
