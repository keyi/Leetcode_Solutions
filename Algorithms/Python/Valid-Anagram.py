class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        dic = collections.defaultdict(int)
        for x in s:
            dic[x] += 1
        for x in t:
            if x not in dic or dic[x] == 0:
                return False
            else:
                dic[x] -= 1
        return sum(dic.values()) == 0
