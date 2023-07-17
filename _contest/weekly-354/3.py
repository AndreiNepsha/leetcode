class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        ln = len(nums)
        dominant = nums[0]
        occ = 1
        for i in range(1, ln):
            if nums[i] == dominant:
                occ += 1
            elif occ == 0:
                occ = 1
                dominant = nums[i]
            else:
                occ -= 1
        
        to_left = 0
        to_right = 0
        for n in nums:
            if n == dominant:
                to_right += 1

        ls, rs = 0, ln
        for r, n in enumerate(nums):
            if r == ln - 1:
                return -1
            ls += 1
            rs -= 1
            if n == dominant:
                to_left += 1
                to_right -= 1
            
            if to_left * 2 > ls and to_right * 2 > rs:
                # print(to_left, ls, to_right, rs)
                return r

        return -1
            