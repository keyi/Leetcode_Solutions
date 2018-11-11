class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        sta = []
        dic = {')': '(', ']': '[', '}': '{'}
        for x in s:
            if sta == []:
                sta.append(x)
            else:
                if x in dic:
                    if dic[x] == sta.pop():
                        continue
                    else:
                        return False
                else:
                    sta.append(x)
        return sta == []
