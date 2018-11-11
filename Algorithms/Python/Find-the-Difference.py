class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.defaultdict(int)
        for x in s:
            dic[x] += 1
        for x in t:
            if x not in dic or dic[x] <= 0:
                return x
            else:
                dic[x] -= 1
