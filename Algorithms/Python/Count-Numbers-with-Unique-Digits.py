class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        ans = 10
        for i in range(1, n):
            temp = 9
            for j in range(1, i + 1):
                temp *= (10 - j)
            ans += temp
        return ans
