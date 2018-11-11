class Solution(object):

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2 or s1[::-1] == s2:
            return True
        if len(s1) != len(s2):
            return False
        m1, m2 = sorted(list(s1)), sorted(list(s2))
        if m1 != m2:
            return False
        l = len(s1)
        for i in range(1, l):
            if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                return True
            if self.isScramble(s1[i:], s2[:l - i]) and self.isScramble(s1[:i], s2[l - i:]):
                return True
        return False
