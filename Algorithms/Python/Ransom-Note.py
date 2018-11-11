class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        dic = collections.defaultdict(int)
        for x in magazine:
            dic[x] += 1
        for x in ransomNote:
            if x not in dic or dic[x] <= 0:
                return False
            else:
                dic[x] -= 1
        return True
