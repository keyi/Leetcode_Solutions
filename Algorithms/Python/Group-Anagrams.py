class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dic = defaultdict(list)
        ans = []
        for x in strs:
            temp = "".join(sorted(x))
            dic[temp].append(x)
        for x in dic.values():
            x.sort()
            ans.append(x)
        return ans
