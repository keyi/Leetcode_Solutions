class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ans, origin = 0, x
        while x != 0:
            ans = 10 * ans + x % 10
            x //= 10
        return ans == origin
