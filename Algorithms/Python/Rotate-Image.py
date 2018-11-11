class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        l = len(matrix)
        for i in range(l):
            for j in range(l - i):
                matrix[i][j], matrix[l - 1 - j][l - 1 -
                                                i] = matrix[l - 1 - j][l - 1 - i], matrix[i][j]
        for i in range(l // 2):
            for j in range(l):
                matrix[i][j], matrix[
                    l - 1 - i][j] = matrix[l - 1 - i][j], matrix[i][j]
