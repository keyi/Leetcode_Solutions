class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        ans = [l - i - 1 for i in range(l + 1)]
        dp = [[False for _ in range(l)] for _ in range(l)]
        for i in reversed(range(l)):
            for j in range(i, l):
                if s[i] == s[j] and (j - 1 < i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans[i] = min(ans[i], ans[j + 1] + 1)
        return ans[0]
