class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        bitmask = 0
        l = -1
        a = 0

        for r, n in enumerate(nums):
            while bitmask & nums[r]:
                l += 1
                bitmask ^= nums[l]
            bitmask |= nums[r]
            
            a = max(a, r - l)
        
        return a
