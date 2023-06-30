class Solution:
    def _isValidSudoku(self, board: list[list[str]]) -> bool:
        def check(hs, he, ws, we):
            present = 0
            for i in range(hs, he):
                for j in range(ws, we):
                    if board[i][j] != ".":
                        k = 1 << int(board[i][j])
                        if k & present:
                            return False
                        else:
                            present = present | k
            return True
        
        # check rows
        for i in range(9):
            if not check(i, i + 1, 0, 9):
                return False
        
        # check columns
        for i in range(9):
            if not check(0, 9, i, i + 1):
                return False
        
        # check squares
        for i in range(3):
            for j in range(3):
                if not check(i * 3, i * 3 + 3, j * 3, j * 3 + 3):
                    return False
        
        return True
    

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        squares = [[0] * 3 for _ in range(3)]
    
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                c = 1 << int(board[i][j])
                if (
                    c & rows[i]
                    or c & columns[j]
                    or c & squares[i // 3][j // 3]
                ):
                    return False
                rows[i] = rows[i] | c
                columns[j] = columns[j] | c
                squares[i // 3][j // 3] = squares[i // 3][j // 3] | c

        return True