class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 0, 1, 2, 4, 6, 9]
        if n <= 6:
            return ans[n]
        for i in range(7, n + 1):
            ans.append(max(ans[i - 2] * 2, ans[i - 3] * 3))
        return ans[n]
