class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = str.strip()
        if s == "" or s[0] not in '+-0123456789':
            return 0
        ans = s[0]
        for x in s[1:]:
            if x in '0123456789':
                ans += x
            else:
                break
        if ans in '-+':
            return 0
        else:
            ans = int(ans)
            if ans > INT_MAX:
                return INT_MAX
            elif ans < INT_MIN:
                return INT_MIN
            else:
                return ans
