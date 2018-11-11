class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for x in s[::-1]:
            flag = -1 if x in 'IXC' and ans >= 5 * dic[x] else 1
            ans += flag * dic[x]
        return ans
