## link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    """
    The idea is to start from pacific and atlantic borders.
    Store the coordinates which could be reached from pacific in a set
    and atlantic in other set.
    Now find the common elements between two sets as result.
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()

        ROWS, COLS = len(heights), len(heights[0])

        def isValidCell(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, prev, visited):
            if (
                not isValidCell(r, c) or 
                heights[r][c] < prev or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        return [list(i) for i in atlantic.intersection(pacific)]

