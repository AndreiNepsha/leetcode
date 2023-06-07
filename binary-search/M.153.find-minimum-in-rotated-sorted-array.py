class Solution:
    def findMin(self, nums: list[int]) -> int:
        ln = len(nums)
        left, right = 0, ln - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


nums = [3, 4, 5, 1, 2]
a = Solution().findMin(nums)
assert 1 == a, a

nums = [4, 5, 6, 7, 0, 1, 2]
a = Solution().findMin(nums)
assert 0 == a, a

nums = [11, 12, 13]
a = Solution().findMin(nums)
assert 11 == a, a
