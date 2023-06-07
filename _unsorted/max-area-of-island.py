from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def _fill_and_get_island_area(i, j):
            area = 0
            island_queue = deque()
            island_queue.append((i, j))
            while len(island_queue) > 0:
                i, j = island_queue.pop()
                if grid[i][j] == 1:
                    area = area + 1
                    grid[i][j] = 2
                if i + 1 < rows and grid[i + 1][j] == 1:
                    island_queue.append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    island_queue.append((i - 1, j))
                if j + 1 < columns and grid[i][j + 1] == 1:
                    island_queue.append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    island_queue.append((i, j - 1))
            return area

        max_area = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    if (area := _fill_and_get_island_area(i, j)) > max_area:
                        max_area = area

        return max_area


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]

max_area = Solution().maxAreaOfIsland(grid)
assert 4 == max_area, max_area
