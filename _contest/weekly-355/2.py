class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)

        a = 0
        l = 0
        for r, n in enumerate(nums):
            while n - k > nums[l] + k:
                l += 1
            a = max(a, r - l + 1)
        return a


a = Solution().maximumBeauty([10,59,86], 23)
assert 2 == a, a

a = Solution().maximumBeauty([4,6,1,2], 2)
assert 3 == a, a
