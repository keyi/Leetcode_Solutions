class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        num, exp, dot = False, False, False
        for i, x in enumerate(s):
            if x.isdigit():
                num = True
            elif x in '+-':
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif x == '.':
                if dot or exp:
                    return False
                dot = True
            elif x == 'e':
                if exp or not num:
                    return False
                exp = True
                num = False
            else:
                return False
        return num
