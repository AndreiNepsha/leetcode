from typing import Callable


class Solution:
    def _bin_search(
        self,
        nums: list[int],
        left: int,
        right: int,
        predicate: Callable[[int], int],
    ) -> int:
        i = None
        while left <= right:
            i = (left + right) // 2
            if predicate(nums[i]) == 1:
                right = i - 1
            elif predicate(nums[i]) == -1:
                left = i + 1
            else:
                return i
        return i

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        elif n == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        else:
            i = self._bin_search(nums, 0, n - 1, lambda x: (x > target) - (x < target))
            if i is None or nums[i] != target:
                return [-1, -1]
            else:
                l = self._bin_search(nums, 0, i, lambda x: 1 if x == target else -1)
                if nums[l] != target:
                    l += 1
                r = self._bin_search(nums, i, n - 1, lambda x: -1 if x == target else 1)
                if nums[r] != target:
                    r -= 1
                return [l, r]


nums = [1, 4]
target = 4
answer = Solution().searchRange(nums, target)
assert [1, 1] == answer, answer


nums = [2, 2]
target = 2
answer = Solution().searchRange(nums, target)
assert [0, 1] == answer, answer

nums = [5, 7, 7, 8, 8, 10]
target = 8
answer = Solution().searchRange(nums, target)
assert [3, 4] == answer, answer

target = 6
answer = Solution().searchRange(nums, target)
assert [-1, -1] == answer, answer

nums = []
answer = Solution().searchRange(nums, target)
assert [-1, -1] == answer, answer
