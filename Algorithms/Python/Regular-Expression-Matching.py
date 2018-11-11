class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        ans = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        ans[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                ans[0][j] = ans[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    ans[i][j] = ans[i][j - 2] or ans[i][j -
                                                        1] or (ans[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    ans[i][j] = ans[i - 1][j -
                                           1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return ans[-1][-1]
