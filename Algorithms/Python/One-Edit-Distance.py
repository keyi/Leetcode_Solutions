# Space O(1), Time O(N)


class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def isOneModified(s, t):
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
            return cnt <= 1

        def isOneDeleted(s, t):
            if len(s) > len(t):
                s, t = t, s
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s == (t[:i] + t[i + 1:])
            return True

        ls, lt = len(s), len(t)
        diff = abs(ls - lt)
        if diff > 1:
            return False
        elif diff == 1:
            return isOneDeleted(s, t)
        else:
            return s != t and isOneModified(s, t)
