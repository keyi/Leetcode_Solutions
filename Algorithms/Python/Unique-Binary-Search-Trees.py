class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1, 1]
        for i in range(2, n + 1):
            temp = 0
            for j in range(1, i + 1):
                temp = temp + ans[j - 1] * ans[i - j]
            ans.append(temp)
        return ans[n]
