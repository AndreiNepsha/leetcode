class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        s = len(nums)
        k = 0
        i = 0
        while i < s:
            if nums[i] != 0:
                nums[k] = nums[i]
                k = k + 1
            i = i + 1
        while k < s:
            nums[k] = 0
            k = k + 1


nums = [0, 1, 2, 0, 3, 0, 7, 12]
Solution().moveZeroes(nums)
assert [1, 2, 3, 7, 12, 0, 0, 0] == nums, nums
