class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            if max_sum < 0:
                cur_sum = n
            elif cur_sum + n > 0:
                cur_sum += n
            else:
                cur_sum = 0
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = Solution().maxSubArray(nums)
assert 6 == a, a

nums = [-2, -1]
a = Solution().maxSubArray(nums)
assert -1 == a, a
