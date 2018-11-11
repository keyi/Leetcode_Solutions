class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            grid[i][j] = 'visited'
            ways = [[i, j - 1], [i, j + 1], [i - 1, j],
                    [i + 1, j]]  # left, right, up, down
            for x in ways:
                row, col = x[0], x[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                    dfs(row, col)

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
