class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = Solution().removeDuplicates(nums)
assert k == 5, k
assert nums == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
