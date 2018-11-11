class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        sideL, sideR, sideU, sideD = -1, n, 0, m
        direction = 0  # 0:right, 1:down, 2:left, 3:up
        ans, i, j = [], 0, 0
        for k in range(m * n):
            ans.append(matrix[i][j])
            if direction == 0:  # go right
                j += 1
                if j == sideR:
                    i += 1
                    j -= 1
                    sideR -= 1
                    direction = 1
            elif direction == 1:  # go down
                i += 1
                if i == sideD:
                    i -= 1
                    j -= 1
                    sideD -= 1
                    direction = 2
            elif direction == 2:  # go left
                j -= 1
                if j == sideL:
                    i -= 1
                    j += 1
                    sideL += 1
                    direction = 3
            elif direction == 3:  # go up
                i -= 1
                if i == sideU:
                    i += 1
                    j += 1
                    sideU += 1
                    direction = 0
        return ans
