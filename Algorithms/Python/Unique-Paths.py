class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            ans[i][0] = 1
        for j in range(n):
            ans[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]
