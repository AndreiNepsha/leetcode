class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        a = -1
        for n in nums:
            if n > 0 and n > a and any(True for k in nums if (k + n) == 0):
                a = n
        return a


nums = [-10, 8, 6, 7, -2, -3]
a = Solution().findMaxK(nums)
assert -1 == a, a

nums = [-1, 10, 6, 7, -7, 1]
a = Solution().findMaxK(nums)
assert 7 == a, a
