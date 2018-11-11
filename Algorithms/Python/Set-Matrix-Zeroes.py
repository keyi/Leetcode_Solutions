class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        first_row = -1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = 0
                    else:
                        matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, row):
            if matrix[i][0] == 0:
                matrix[i] = [0] * col
        for j in range(col):
            if matrix[0][j] == 0:
                for i in range(row):
                    matrix[i][j] = 0
        if first_row == 0:
            matrix[0] = [0] * col
