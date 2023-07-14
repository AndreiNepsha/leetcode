class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        n = len(arr)
        dp = {}

        mx = 1
        for n in arr:
            prev = n - difference
            if prev not in dp:
                dp[n] = 1
            else:
                dp[n] = dp[prev] + 1
                mx = max(mx, dp[n])
        
        return mx
