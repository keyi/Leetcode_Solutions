class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[0 for x in range(n)] for x in range(m)]
        flag = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                flag = True
            ans[i][0] = 0 if flag else 1
        flag = False
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                flag = True
            ans[0][j] = 0 if flag else 1
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = 0 if obstacleGrid[i][
                    j] == 1 else ans[i - 1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]
