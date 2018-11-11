class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = [[0 for x in range(n)] for x in range(m)]
        ans[0][0] = grid[0][0]
        for i in range(1, m):
            ans[i][0] = ans[i - 1][0] + grid[i][0]
        for j in range(1, n):
            ans[0][j] = ans[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + grid[i][j]
        return ans[m - 1][n - 1]
