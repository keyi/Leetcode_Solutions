class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n != 0:
            ans = chr((n - 1) % 26 + 65) + ans
            n = (n - 1) // 26
        return ans
