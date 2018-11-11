class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def memorize(i, j):
            if s[i][j]:
                return s[i][j]
            ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in ways:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    s[i][j] = max(s[i][j], memorize(x, y))
            s[i][j] += 1
            return s[i][j]

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        s = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, memorize(i, j))
        return ans
