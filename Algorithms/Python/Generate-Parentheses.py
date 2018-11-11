class Solution:
    # @param an integer
    # @return a list of string

    def generateParenthesis(self, n):

        def dfs(cur, left, right):
            if left == 0 and right == 0:
                ans.append(cur)
                return
            if left > right or left < 0 or right < 0:
                return
            dfs(cur + '(', left - 1, right)
            dfs(cur + ')', left, right - 1)

        ans = []
        dfs('', n, n)
        return ans
