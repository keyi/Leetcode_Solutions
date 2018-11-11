class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if i and j and matrix[i][j] != '0':
                    matrix[i][j] = str(
                        min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]), int(matrix[i][j - 1])) + 1)
                ans = max(ans, int(matrix[i][j]))
        return ans * ans
