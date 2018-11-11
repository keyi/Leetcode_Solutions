class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            if s[start].lower() not in 'aeiou':
                start += 1
            if s[end].lower() not in 'aeiou':
                end -= 1
            if s[start].lower() in 'aeiou' and s[end].lower() in 'aeiou':
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)
