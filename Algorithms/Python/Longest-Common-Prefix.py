class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        index, minLen = -1, 2147483647
        for i in range(len(strs)):
            if len(strs[i]) < minLen:
                minLen = len(strs[i])
                index = i
        ans, s = "", strs[index]
        for i in range(len(s)):
            temp = s[i]
            for x in strs:
                if x[i] != temp:
                    return s[:i]
            ans = s[:i + 1]
        return ans
