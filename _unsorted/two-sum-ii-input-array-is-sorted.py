class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if (s := numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1


numbers = [1, 2, 7, 8, 11, 99, 101]
target = 16
a = Solution().twoSum(numbers, target)
assert [2, 5] == a, a
