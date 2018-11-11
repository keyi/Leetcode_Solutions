class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(j):
            for i in range(j):
                if s[i] == s[j] or abs(i - j) == abs(s[i] - s[j]):
                    return False
            return True

        def dfs(pos):
            if pos == self.n:
                temp = [''] * self.n
                for i in range(self.n):
                    temp[i] = '.' * s[i] + 'Q' + '.' * (self.n - s[i] - 1)
                ans.append(temp)
                return
            for k in range(self.n):
                s[pos] = k
                if isValid(pos):
                    dfs(pos + 1)
                s[pos] = -1

        ans = []
        self.n = n
        s = [-1] * self.n
        dfs(0)
        return ans
