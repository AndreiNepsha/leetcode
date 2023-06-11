class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        s = sorted(nums)
        n = 1
        for i in range(1, len(nums)):
            if s[i] != s[i - 1]:
                n += 1
            if n == 3:
                return s[i - 1]
        return -1
