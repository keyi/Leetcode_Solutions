class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans, dic = [], {x: 1 for x in nums1}
        for x in nums2:
            if x in dic and dic[x] == 1:
                ans.append(x)
                dic[x] = 0
        return ans
