class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = 1
        dic = {x: 0 for x in nums}
        for x in nums:
            if dic[x] == 0:
                dic[x] = 1
                small, big = dic.get(x - 1, 0), dic.get(x + 1, 0)
                curlen = small + 1 + big
                dic[x - small], dic[x + big] = curlen, curlen
                ans = max(ans, curlen)
        return ans
