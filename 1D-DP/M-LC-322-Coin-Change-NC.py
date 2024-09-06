## link: https://leetcode.com/problems/coin-change/description/

class Solution:
    """
    If we use top down approach, starting from amount = 7,
    we need to calculate using dfs and backtracking and use memoization
    dp[a] = min(dp[a], 1 + dfs(a-c)) for c in coins
    if a way exists we will get a number else inf.

    This way we go down to zero. But its still a heavy one.

    So we use bottom up approach. We start from 1 to amount
    For each amount starting from 1,we try to use all the coins
    If we could use a coin, the condition would be a - c >= 0
    So we update the dp[a] = min(dp[a], 1 + dp[a - c])
    since a - c is greater than equal to 0 it will be equal to amount already process
    before in the loop. So if there are coins which could create those amounts we take that 
    and add 1 to it indicating 1 coin + coins for a -c amount, ele it will be inf and we dont consider it.

    """ 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1




