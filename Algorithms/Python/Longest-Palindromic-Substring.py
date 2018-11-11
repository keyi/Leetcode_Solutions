class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans, maxLen, l = s[0], 0, len(s)
        for i in range(l):
            count = 1
            left, right = i - 1, i + 1
            while left >= 0 and right < l and s[left] == s[right]:
                count += 2
                left -= 1
                right += 1
            if count > maxLen:
                maxLen = count
                ans = s[left + 1:right]
            if i + 1 < l and s[i] == s[i + 1]:
                count = 2
                left, right = i - 1, i + 2
                while left >= 0 and right < l and s[left] == s[right]:
                    count += 2
                    left -= 1
                    right += 1
                if count > maxLen:
                    maxLen = count
                    ans = s[left + 1:right]
        return ans


# METHOD 2
# when you increase s by 1 character,
# you could only increase maxPalindromeLen by either 1 or 2,
# and that new maxPalindrome includes this new character.
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        maxLen = 1
        for i in range(1, len(s)):
            # by 1
            if s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
            # by 2
            elif i - maxLen > 0 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
        return s[start:start + maxLen]
