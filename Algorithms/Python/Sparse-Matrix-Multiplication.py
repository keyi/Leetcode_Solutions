# A is m x n matrix, B is n x l matrix
# Space: O(m * l), Time:  O(m * n * l)


class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, l = len(A), len(A[0]), len(B[0])
        ans = [[0 for _ in range(l)] for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in range(l):
                        ans[i][j] += A[i][k] * B[k][j]
        return ans
