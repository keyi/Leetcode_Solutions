class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getStatus(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            else:
                return board[i][j] & 1
        m, n = len(board), len(board[0])
        row = [-1, -1, -1, 0, 0, 1, 1, 1]
        col = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                status = 0
                for k in range(8):
                    status += getStatus(i + row[k], j + col[k])
                if (board[i][j] and 2 <= status and status <= 3) or status == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
# METHOD 2


class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getCount(matrix, row, col):
            m, n = len(matrix), len(matrix[0])
            count = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i < 0 or i >= m or j < 0 or j >= n or (i == row and j == col):
                        continue
                    elif matrix[i][j] == 1:
                        count += 1
            return count

        m, n = len(board), len(board[0])
        pre = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = getCount(pre, i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                elif count == 3:
                    board[i][j] = 1
