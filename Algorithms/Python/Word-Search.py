class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def isValid(board, i, j, target):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#' or board[i][j] != target:
                return False
            return True

        def dfs(board, i, j, cur, pos):
            if cur == word:
                return True
            if len(cur) >= len(word):
                return False
            ways = [[i, j - 1], [i, j + 1], [i - 1, j],
                    [i + 1, j]]  # [left, right,up,left]
            for x in ways:
                row, col = x[0], x[1]
                if isValid(board, row, col, word[pos]):
                    temp, board[row][col] = board[row][col], '#'
                    if dfs(board, row, col, cur + temp, pos + 1):
                        return True
                    board[row][col] = temp
            return False

        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if dfs(board, i, j, word[0], 1):
                        return True
                    board[i][j] = word[0]

        return False
