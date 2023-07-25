class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [amount + 1] * (amount + 1)
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for a in range(1, amount + 1):
            for c in coins:
                if a - c > 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[amount] if dp[amount] < amount + 1 else -1
