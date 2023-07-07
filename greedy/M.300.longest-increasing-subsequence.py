class Solution:
    # time - O(n^2), space - O(n)
    def _lengthOfLIS(self, nums: list[int]) -> int:
        ln = len(nums)
        dp = [0] * ln
        
        for i, n in enumerate(nums):
            for j in range(i):
                if nums[j] < n and dp[j] > dp[i]:
                    dp[i] = dp[j]
            dp[i] += 1

        return max(dp)

    # time - O(n*log(n)), space - O(n)
    def lengthOfLIS(self, nums: list[int]) -> int:
        ln = len(nums)
        sub = []

        def search(target: int, ) -> int:
            left, right = 0, len(sub) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if mid == right:
                    return mid
                if sub[mid] < target:
                    left = mid + 1
                elif sub[mid] >= target:
                    right = mid
        
        for n in nums:
            if not len(sub) or n > sub[-1]:
                sub.append(n)
            else:
                sub[search(n)] = n

        return len(sub)


a = Solution().lengthOfLIS(nums = [2, 6, 8, 3, 4, 5, 1])
assert 4 == a, a
