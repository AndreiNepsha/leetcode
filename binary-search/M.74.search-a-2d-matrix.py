class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lm = m * n

        left, right = 0, lm - 1

        while left <= right:
            mid = left + (right - left) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True
        return False


nums = [[4]]
target = 4
a = Solution().searchMatrix(nums, target)
assert a

nums = [[7]]
target = 4
a = Solution().searchMatrix(nums, target)
assert not a

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
a = Solution().searchMatrix(matrix, target)
assert a

nums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
a = Solution().searchMatrix(nums, target)
assert not a
