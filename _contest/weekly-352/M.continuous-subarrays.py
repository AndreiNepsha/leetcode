class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        ln =  len(nums)
        if max(nums) - min(nums) <= 2:
            return (ln * (ln + 1)) // 2

        a = 1
        start, end = 0, 0
        mx, mn = nums[0], nums[0]
        while end < ln - 1:
            end = end + 1
            if abs(nums[end] - mx) <= 2 and abs(nums[end] - mn) <= 2:
                mx, mn = max(nums[end], mx), min(nums[end], mn)
            else:
                start = end
                mx, mn = nums[end], nums[end]
                while start > 0 and abs(nums[start - 1] - mx) <= 2 and abs(nums[start - 1] - mn) <= 2:
                    start = start - 1
                    mx, mn = max(nums[start], mx), min(nums[start], mn)
            a += end - start + 1
        return a


a = Solution().continuousSubarrays(nums = [65,66,65,64,63,62,62])
assert 20 == a, a

a = Solution().continuousSubarrays(nums = [5,4,2,4])
assert 8 == a, a

a = Solution().continuousSubarrays(nums = [31,30,31,32])
assert 10 == a, a

a = Solution().continuousSubarrays(nums = [65,66,67,66,66,65,64,65,65,64])
assert 43 == a, a