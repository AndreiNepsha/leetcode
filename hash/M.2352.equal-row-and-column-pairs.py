from collections import Counter


class Solution:
    def _equalPairs(self, grid: list[list[int]]) -> int:
        equal_rows_counter = Counter(["".join([str(c) for c in r]) for r in grid])
        r = 0
        for k in range(len(grid)):
            c = "".join([str(grid[i][k]) for i in range(len(grid))])
            if c in equal_rows_counter:
                r += equal_rows_counter[c]
        return r
    
    # faster solution
    def equalPairs(self, grid: list[list[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        for tpl in zip(*grid):
            pairs += cnt[tpl]
        return pairs
    

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
a = Solution().equalPairs(grid)
assert 3 == a, a
