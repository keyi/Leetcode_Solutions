class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validSo(i, j):
            for row in range(9):
                if row != i and board[row][j] == board[i][j]:
                    return False
            for col in range(9):
                if col != j and board[i][col] == board[i][j]:
                    return False
            for r in range(3):
                for c in range(3):
                    row = (i // 3) * 3 + r
                    col = (j // 3) * 3 + c
                    if row != i and col != j and board[row][col] == board[i][j]:
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif not validSo(i, j):
                    return False
        return True
