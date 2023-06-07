from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def _fill_island(i, j):
            island_queue = deque()
            island_queue.append((i, j))
            isolated = True
            while len(island_queue) > 0:
                i, j = island_queue.pop()
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    if i + 1 == rows or i - 1 < 0 or j + 1 == columns or j - 1 < 0:
                        isolated = False
                if i + 1 < rows and grid[i + 1][j] == 0:
                    island_queue.append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    island_queue.append((i - 1, j))
                if j + 1 < columns and grid[i][j + 1] == 0:
                    island_queue.append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    island_queue.append((i, j - 1))
            return isolated

        islands = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    if _fill_island(i, j):
                        islands = islands + 1

        return islands


grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
a = Solution().closedIsland(grid)
assert 2 == a, a
