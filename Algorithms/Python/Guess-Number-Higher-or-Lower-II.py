class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(left, right):
            if left >= right:
                return 0
            if dp[left][right]:
                return dp[left][right]
            dp[left][right] = min(
                i + max(solve(left, i - 1), solve(i + 1, right)) for i in range(left, right + 1))
            return dp[left][right]

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return solve(1, n)
