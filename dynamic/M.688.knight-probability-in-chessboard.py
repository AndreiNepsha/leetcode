class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        Q = 0.125
        MOVES = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        NEXT_MAP = {
            (i, j): [
                (i + di, j + dj) for di, dj in MOVES if 0 <= i + di < n and 0 <= j + dj < n
            ] for i in range(n) for j in range(n)
        }

        mtx = [[1] * n for _ in range(n)]

        for _ in range(k):
            k_mtx = [[1] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if mtx[i][j] == 0:
                        continue
                    prob = 0
                    for ni, nj in NEXT_MAP[(i, j)]:
                        prob += Q * mtx[ni][nj]
                    k_mtx[i][j] = prob
            mtx = k_mtx

        return mtx[row][column]
