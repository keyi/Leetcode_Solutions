class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        dic = collections.defaultdict(int)
        ans = []
        for x in nums1:
            dic[x] += 1
        for x in nums2:
            if x in dic and dic[x] > 0:
                dic[x] -= 1
                ans.append(x)
        return ans
