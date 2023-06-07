class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        dups = False
        for i in range(1, len(nums)):
            if nums[i] != nums[k] or not dups:
                if nums[i] != nums[k]:
                    dups = False
                else:
                    dups = True
                k += 1
                nums[k] = nums[i]
        return k + 1
