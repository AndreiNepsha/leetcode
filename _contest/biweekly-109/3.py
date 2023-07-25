# TODO PROOF
class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = nums[0]
        js = 0
        for i in range(1, n):
            for j in range(js, i):
                same_parties = (nums[i] + nums[j]) % 2 == 0
                dp[i] = max(dp[i], dp[j] + nums[i] if same_parties else dp[j] + nums[i] - x)
            while dp[j] > dp[js] + x:
                js += 1
        return max(dp)
        

a = Solution().maxScore([9,58,17,54,91,90,32,6,13,67,24,80,8,56,29,66,85,38,45,13,20,73,16,98,28,56,23,2,47,85,11,97,72,2,28,52,33], 90)
assert 886 == a, a
