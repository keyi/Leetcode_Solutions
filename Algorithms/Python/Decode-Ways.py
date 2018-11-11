class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        ans = [1, 1]
        for i in range(2, len(s) + 1):
            temp = int(s[i - 2:i])
            if temp == 10 or temp == 20:
                cur = ans[i - 2]
            elif 10 < temp and temp <= 26:
                cur = ans[i - 2] + ans[i - 1]
            elif s[i - 1] != '0':
                cur = ans[i - 1]
            else:
                return 0
            ans.append(cur)
        return ans[-1]
