class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        s = preorder.split(',')
        if s.count('#') * 2 - 1 != len(s):
            return False
        level = 1
        for x in s:
            level -= 1
            if level < 0:
                return False
            if x != '#':
                level += 2
        return True


# METHOD 2


class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        s = []
        for x in preorder.split(','):
            s += [x]
            while len(s) >= 3 and s[-3] != '#' and s[-2:] == ['#', '#']:
                s = s[:-3] + ['#']
        return s == ['#']
