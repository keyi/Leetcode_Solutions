class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
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

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            board[i][j] = num
                            if validSo(i, j) and solve():
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solve()
