class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        ln = len(nums)
        presented = [False] * ln
        for i in range(ln):
            if nums[i] <= ln and nums[i] >= 1:
                presented[nums[i] - 1] = True
        for i in range(ln):
            if not presented[i]:
                return i + 1
        return ln + 1

# 6 2 7 3 0 1
