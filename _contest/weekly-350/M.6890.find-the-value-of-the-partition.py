class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        nums = sorted(nums)
        return min(nums[i] - nums[i - 1] for i in range(1, len(nums)))


a = Solution().findValueOfPartition(nums = [59,51,1,98,73])
assert 8 == a, a

a = Solution().findValueOfPartition(nums = [1,3,2,4])
assert 1 == a, a

a = Solution().findValueOfPartition(nums = [100,1,10])
assert 9 == a, a

