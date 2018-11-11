class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = -1
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    last = i
                else:
                    stack.pop()
                    if stack:
                        ans = max(ans, i - stack[-1])
                    else:
                        ans = max(ans, i - last)
        return ans
