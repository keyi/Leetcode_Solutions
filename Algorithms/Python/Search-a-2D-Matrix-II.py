class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                j -= 1
            else:
                i += 1
        return False
