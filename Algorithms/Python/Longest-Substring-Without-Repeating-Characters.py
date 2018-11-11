class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, temp = 0, ''
        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
                if len(temp) > ans:
                    ans = len(temp)
            else:
                k = temp.find(s[i])
                temp = temp[k + 1:] + s[i]
        return ans
