class Solution(object):

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        s = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)
