class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for x in s:
                if x == '(':
                    cnt += 1
                elif x == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        def getParentheses(s):
            left, right = 0, 0
            for x in s:
                if x == '(':
                    left += 1
                elif x == ')':
                    if left:
                        left -= 1
                    else:
                        right += 1
            return (left, right)

        def dfs(start, left, right):
            if left == 0 and right == 0:
                temp = ''
                for i, x in enumerate(s):
                    if i not in removed:
                        temp += x
                if isValid(temp):
                    ans.append(temp)
                return
            for i in range(start, len(s)):
                if right == 0 and left > 0 and s[i] == '(':
                    if i == start or s[i] != s[i - 1]:
                        removed[i] = True
                        dfs(i + 1, left - 1, right)
                        del removed[i]
                elif right > 0 and s[i] == ')':
                    if i == start or s[i] != s[i - 1]:
                        removed[i] = True
                        dfs(i + 1, left, right - 1)
                        del removed[i]

        ans, removed = [], {}
        left, right = getParentheses(s)
        dfs(0, left, right)
        return ans
