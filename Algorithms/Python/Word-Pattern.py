class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s, dic = str.split(' '), {}
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] in dic.values():
                    return False
                dic[pattern[i]] = s[i]
            else:
                if dic[pattern[i]] != s[i]:
                    return False
        return True
