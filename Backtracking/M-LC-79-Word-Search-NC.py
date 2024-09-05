## link: https://leetcode.com/problems/word-search/description/

class Solution:
    """
    The intuition is to use backtracking from the starting letter of the word.
    We backtrack and check for each letter till we reach the end.
    The trick here is to remove the current element from path once all neighbours are computed.
    Since once we return we no longer process on that element, we explore other paths.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def isValidCell(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, i, path):
            if i == len(word):
                return True
            if not isValidCell(r, c) or (r, c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1, path) or
                dfs(r - 1, c, i + 1, path) or
                dfs(r, c + 1, i + 1, path) or 
                dfs(r, c - 1, i + 1, path))

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()): return True
        
        return False
                