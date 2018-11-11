# METHOD 1: DP  Time(M*N), Space(M*N)


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
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                ans[0][j] = ans[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    ans[i][j] = ans[i - 1][j] or ans[i][j - 1]
                else:
                    ans[i][j] = ans[i - 1][j -
                                           1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        return ans[-1][-1]


# METHOD 2: Iteration  Time(N), Space(1)


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        Idxs, Idxp = 0, 0
        Lasts, Lastp = -1, -1
        ls, lp = len(s), len(p)
        while Idxs < ls:
            if Idxp < lp and (s[Idxs] == p[Idxp] or p[Idxp] == '?'):
                Idxs += 1
                Idxp += 1
            elif Idxp < lp and p[Idxp] == '*':
                Idxp += 1
                Lasts, Lastp = Idxs, Idxp
            elif Lastp != -1:
                Lasts += 1
                Idxs = Lasts
                Idxp = Lastp
            else:
                return False
        for i in range(Idxp, lp):
            if p[i] != '*':
                return False
        return True
