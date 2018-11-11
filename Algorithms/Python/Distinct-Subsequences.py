# METHOD 1: Time(M*N) Space (M*N)


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t), len(s)
        if m > n:
            return 0
        ans = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans[0] = [1] * n
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1] + ans[i][j - 1]
                else:
                    ans[i][j] = ans[i][j - 1]
        return ans[-1][-1]


# METHOD 2: Time(M*N) Space (N)


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t), len(s)
        if m > n:
            return 0
        dp = [1] * (n + 1)
        for i in range(1, m + 1):
            upleft = dp[0]
            dp[0] = 0
            for j in range(1, n + 1):
                temp = dp[j]
                dp[j] = dp[j - 1]
                if t[i - 1] == s[j - 1]:
                    dp[j] += upleft
                upleft = temp
        return dp[-1]
