class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == 'O':
                queue.append([i, 0])
            if board[i][n - 1] == 'O':
                queue.append([i, n - 1])
        for j in range(n):
            if board[0][j] == 'O':
                queue.append([0, j])
            if board[m - 1][j] == 'O':
                queue.append([m - 1, j])

        while queue:
            cur = queue.pop(0)
            i, j = cur[0], cur[1]
            board[i][j] = '#'
            ways = [[i, j - 1], [i, j + 1], [i - 1, j],
                    [i + 1, j]]  # left, right, up, down
            for x in ways:
                row, col = x[0], x[1]
                if 0 <= row < m and 0 <= col < n and board[row][col] == 'O':
                    queue.append([row, col])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
