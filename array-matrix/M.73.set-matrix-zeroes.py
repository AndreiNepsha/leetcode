class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        col_0 = 1
        
        for i in range(n):
            if matrix[i][0] == 0:
                col_0 = 0
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if col_0 == 0:
                matrix[i][0] = 0
