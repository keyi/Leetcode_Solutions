class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        flag = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            ans = 10 * ans + x % 10
            x //= 10
        ans = flag * ans
        return 0 if ans >= 2147483647 or ans < -2147483648 else ans
