class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        def dfs(amnt):
            if amnt == 0:
                return 0
            if memo[amnt] != -1:
                return memo[amnt]

            res = 1e9
            for coin in coins:
                if amnt - coin >= 0:
                    res = min(res, 1 + dfs(amnt - coin))
            memo[amnt] = res
            return memo[amnt]
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins