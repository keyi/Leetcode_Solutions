class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isValid(j):
            for i in range(j):
                if s[i] == s[j] or abs(i - j) == abs(s[i] - s[j]):
                    return False
            return True

        def dfs(pos):
            if pos == self.n:
                self.cnt += 1
                return
            for k in range(self.n):
                s[pos] = k
                if isValid(pos):
                    dfs(pos + 1)
                s[pos] = -1

        self.cnt = 0
        self.n = n
        s = [-1] * self.n
        dfs(0)
        return self.cnt
