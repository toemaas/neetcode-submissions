class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 12 - 10 = 2
        # min amnt to make 12: dfs(12 - 10)
        # dfs(12 - 5)
        # dfs(12 - 1)
        # base case: 0
        # base case: amnt - coin >= 0
        # memo[i] = min coins to make i amnt
        memo = {}

        def dfs(amnt):
            if amnt == 0:
                return 0
            if amnt in memo:
                return memo[amnt]
            
            res = 1e9
            for coin in coins:
                if amnt - coin >= 0:
                    res = min(res, 1 + dfs(amnt - coin))
            
            memo[amnt] = res
            return res
        
        minCoins = dfs(amount)

        return minCoins if minCoins < 1e9 else -1
            