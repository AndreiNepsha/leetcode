class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        longest = -1
        cur = 1
        last = nums[0]
        alt = -1

        for i in range(1, len(nums)):
            if last - nums[i] == alt:
                cur += 1
                alt = -alt
                longest = max(longest, cur)
            else:
                if nums[i - 1] - nums[i] == -1:
                    cur = 2
                    alt = 1
                else:
                    cur = 1
                    alt = -1
            last = nums[i]
        return longest


a = Solution().alternatingSubarray(nums = [2,3,4,3,4])
assert 4 == a, a

a = Solution().alternatingSubarray(nums = [4,5,6])
assert 2 == a, a

a = Solution().alternatingSubarray(nums = [14,30,29,49,3,23,44,21,26,52])
assert -1 == a, a

