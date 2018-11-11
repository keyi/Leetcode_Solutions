class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True

        ans = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                ans[i] = True
                continue
            for j in range(i):
                if ans[j] and s[j + 1:i + 1] in wordDict:
                    ans[i] = True
                    break
        return ans[-1]
