class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix), len(matrix[0])
        si, ei = 0, n - 1
        sj, ej = 0, m - 1

        spiral = [None] * (n * m)

        k = 0
        while si <= ei and sj <= ej:
            for j in range(sj, ej + 1):
                spiral[k] = matrix[si][j]
                k += 1
            si += 1
            for i in range(si, ei + 1):
                spiral[k] = matrix[i][ej]
                k += 1
            ej -= 1
            if si <= ei:
                for j in range(ej, sj - 1, -1):
                    spiral[k] = matrix[ei][j]
                    k += 1
                ei -= 1
            if sj <= ej:
                for i in range(ei, si - 1, -1):
                    spiral[k] = matrix[i][sj]
                    k += 1
                sj += 1
        
        return spiral


a = Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
assert [1,2,3,6,9,8,7,4,5] == a, a

a = Solution().spiralOrder(matrix = [[1,2,3]])
assert [1,2,3] == a, a

a = Solution().spiralOrder(matrix = [[1],[2],[3]])
assert [1,2,3] == a, a
