class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        ranges = []
        s, e = nums[0], nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                ranges.append(f"{s}->{e}" if e - s > 0 else f"{s}")
                s, e = nums[i + 1], nums[i + 1]
            else:
                e = nums[i + 1]
        ranges.append(f"{s}->{e}" if e - s > 0 else f"{s}")

        return ranges

nums = [0,1,2,4,5,7]
a = Solution().summaryRanges(nums)
assert ["0->2","4->5","7"] == a, a
