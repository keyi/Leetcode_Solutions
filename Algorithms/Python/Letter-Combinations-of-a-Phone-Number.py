class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(cur, pos):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            temp = digits[pos:]
            for i in range(len(temp)):
                for x in dic[temp[i]]:
                    dfs(cur + x, pos + i + 1)
        if not digits:
            return []
        ans = []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        dfs('', 0)
        return ans
