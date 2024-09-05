## link: https://leetcode.com/problems/word-search/

class Solution:
    """
    The problem here is there should be no duplicates.
    So we recursively take two decisions at each step.
    We follow the index that we are looking at each step.

    We either include the current element and dont increase the index, as 
    we can use same element multiple times.
    And we exclude current element in current and next steps of that decision tree
    by increasing the index.

    By this we recur until we reach the base cases.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res