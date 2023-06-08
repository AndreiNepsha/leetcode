class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, k = 0, n - 1
        negatives = 0
        while i < m:
            while k >= 0 and grid[i][k] < 0:
                k -= 1
            negatives += n - k - 1
            i += 1
        return negatives


assert 8 == Solution().countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
