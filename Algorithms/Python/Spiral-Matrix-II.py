class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for x in range(n)] for x in range(n)]
        sideL, sideR, sideU, sideD = -1, n, 0, n
        i, j = 0, 0
        direction = 0  # 0:right, 1:down, 2:left, 3:up
        for k in range(n * n):
            ans[i][j] = k + 1
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
