class Solution:
    def rob(self, nums: list[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return nums[0]
        elif ln == 2:
            return max(nums)
        
        mr = [nums[0], max(nums[:2])]
        mr.append(max(nums[0] + nums[2], nums[1]))
        for i in range(3, ln):
            mr.append(max([
                nums[i] + mr[i - 2],
                nums[i] + mr[i - 3],
            ]))
        print(mr)
        return max(mr[-3:])


# nums = [2, 7, 9, 14, 1]
# nums = [1, 7, 1, 2, 7]
nums = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
a = Solution().rob(nums)
assert 4517 == a, a
