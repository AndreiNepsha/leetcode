class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ln = len(nums)
        left, right = 0, ln - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


nums = [0, 1, 2, 3, 4, 5, 6, 7]
target = 0
a = Solution().search(nums, target)
assert 0 == a, a

nums = [0, 1, 2, 3, 4, 5, 6, 7]
target = 5
a = Solution().search(nums, target)
assert 5 == a, a

nums = [1]
target = 5
a = Solution().search(nums, target)
assert -1 == a, a
