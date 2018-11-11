class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end, flag = 0, 0, True
        for i in range(len(s)):
            if s[i] != ' ':
                if flag:
                    start = i
                    flag = False
                end = i
        s = s[start:end + 1]
        if s == ' ':
            return ''
        start, flag = 0, True
        ans = []
        for i in range(1, len(s)):
            if s[i] == ' ' and flag:
                flag = False
                ans.append(s[start:i])
            elif s[i - 1] == ' ' and s[i] != ' ':
                flag = True
                start = i
        ans.append(s[start:len(s)])
        return ' '.join([x for x in ans[::-1]])


# METHOD 2


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split(' ')
        return " ".join([x for x in s[::-1] if x])
