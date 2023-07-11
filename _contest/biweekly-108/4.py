class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> int:
        coordinates = {(c[0], c[1]) for c in coordinates}

        res = [0] * 5
        calculated = set()
        
        for c in coordinates:
            row, col = c
            for i in (max(row - 1, 0), min(row, m - 2)):
                for j in (max(col - 1, 0), min(col, n - 2)):
                    if (i, j) not in calculated:
                        calculated.add((i, j))
                        c = 0
                        if (i, j) in coordinates:
                            c += 1
                        if (i + 1, j) in coordinates:
                            c += 1
                        if (i, j + 1) in coordinates:
                            c += 1
                        if (i + 1, j + 1) in coordinates:
                            c += 1
                        res[c] += 1
        
        res[0] += (m - 1) * (n - 1) - sum(res)

        return res

a = Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]])
assert [0,2,2,0,0] == a, a

a = Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0]])
assert [3,1,0,0,0] == a, a


a = Solution().countBlackBlocks(32, 32, [[17,29],[29,16],[19,20],[18,9],[16,7],[20,25],[22,19],[4,9],[14,17],[6,23],[2,2],[20,1],[8,7],[4,7],[14,14],[10,10],[1,27],[18,23],[6,30],[8,18],[26,23],[25,8],[5,6],[3,4]])
assert [866,94,1,0,0] == a, a

