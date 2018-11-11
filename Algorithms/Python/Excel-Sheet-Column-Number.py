class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for x in s:
            ans = ans * 26 + ord(x) - 64
        return ans
