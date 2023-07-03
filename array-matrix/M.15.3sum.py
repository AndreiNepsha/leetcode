class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ln = len(nums)
        li = ln - 1
        nums = sorted(nums)
        first_pos = 0
        while first_pos < ln and nums[first_pos] <= 0:
            first_pos = first_pos + 1

        out = []
        i = 0
        p = li
        while i < first_pos:
            j = i + 1
            while j < li:
                target = - (nums[i] + nums[j])
                if target < nums[p]:
                    while j < p and target < nums[p]:
                        p = p - 1
                elif target > nums[p]:
                    while p < li and target > nums[p]:
                        p = p + 1
                if j != p and target == nums[p]:
                    out.append([nums[i], nums[j], target])
                while j < p and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < li and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return out

print(ord("a"))

a = Solution().threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4])
assert [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]] == a, a

a = Solution().threeSum(nums = [-1,0,1,2,-1,-4])
assert [[-1,-1,2],[-1,0,1]] == a, a

a = Solution().threeSum(nums = [0, 0, 0])
assert [[0,0,0]] == a, a

a = Solution().threeSum(nums = [1,1,-2])
assert [[-2, 1,1]] == a, a

a = Solution().threeSum(nums = [-2,0,0,2,2])
assert [[-2, 0, 2]] == a, a