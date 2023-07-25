class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        dp = [1] + [0] * n

        k = 1
        while (cur := k ** x) <= n:
            for j in range(n, cur - 1, -1):
                if j - cur:
                    dp[j] = (dp[j] + dp[j - cur]) % MOD
            dp[cur] += 1
            k += 1

        return dp[n]


a = Solution().numberOfWays(n = 10, x = 2)
assert 1 == a, a

a = Solution().numberOfWays(n = 4, x = 1)
assert 2 == a, a

a = Solution().numberOfWays(n = 3, x = 1)
assert 2 == a, a

a = Solution().numberOfWays(n = 30, x = 1)
assert 296 == a, a

a = Solution().numberOfWays(n = 90, x = 1)
assert 189586 == a, a

a = Solution().numberOfWays(n = 300, x = 1)
assert 872471266 == a, a

a = Solution().numberOfWays(n = 30, x = 2)
assert 2 == a, a
