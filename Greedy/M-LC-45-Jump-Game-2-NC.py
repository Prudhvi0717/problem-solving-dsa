## link: https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    """
    The approach is to find the levels.
    A level is like, lets assume we are at first index in the arr [2, 3, 1, 1, 4]
    2 is our first level = 0
    From that level we could go to next level of index range 1 to 2
    that would be our second level.
    From that level we could go next level of index range 3 to 4.

    Here each level denotes the steps we need to take.
    By calculating in iterative BFS technique we can get the min steps.
    Take two pointer l and r
    place them at the min and max index of next level range.
    Iterate through each level range and update the fathest we could go from that level.
    l will become r + 1
    and r becomes the farthest. Once r crosses last index, we got the answer.
    """
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            res += 1
            l = r + 1
            r = farthest
        return res