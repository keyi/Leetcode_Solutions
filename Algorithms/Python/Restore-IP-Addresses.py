class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(cur, pos):
            if len(cur) == 4 and pos == len(s):
                ans.append('.'.join(cur))
                return
            elif len(cur) == 4 or pos == len(s):
                return
            temp = s[pos:]
            for i in range(len(temp)):
                x = temp[:i + 1]
                if int(x) < 256 and (len(x) == 1 or x[0] != '0'):
                    dfs(cur + [x], pos + i + 1)

        ans = []
        dfs([], 0)
        return ans
