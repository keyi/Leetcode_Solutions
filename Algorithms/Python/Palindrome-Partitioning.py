class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(cur, pos):
            if len(''.join(cur)) == len(s):
                ans.append(cur)
                return
            temp = s[pos:]
            for i in range(len(temp)):
                if temp[:i + 1] == temp[:i + 1][::-1]:
                    dfs(cur + [temp[:i + 1]], pos + i + 1)

        if not s:
            return []
        ans = []
        dfs([], 0)
        return ans
