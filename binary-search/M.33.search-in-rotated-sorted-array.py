class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ln = len(nums)
        if ln == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, ln - 1
        k = right
        while k > 0 and nums[k] > nums[k - 1]:
            k -= 1

        while left <= right:
            mid = left + (right - left) // 2
            kmid = mid + k if mid + k < ln else mid + k - ln
            if nums[kmid] < target:
                left = mid + 1
            elif nums[kmid] > target:
                right = mid - 1
            else:
                return kmid
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
a = Solution().search(nums, target)
assert 4 == a, a

nums = [1, 3]
target = 1
a = Solution().search(nums, target)
assert 0 == a, a

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
a = Solution().search(nums, target)
assert -1 == a, a

nums = [1]
target = 5
a = Solution().search(nums, target)
assert -1 == a, a
