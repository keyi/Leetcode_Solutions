class Solution(object):

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def get_max_subarray(nums, k):
            s, l = [], len(nums)
            for i, x in enumerate(nums):
                while s and s[-1] < x and l - i > k - len(s):
                    s.pop()
                if len(s) < k:
                    s.append(x)
            return s

        ans = 0
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            arr1 = get_max_subarray(nums1, i)
            arr2 = get_max_subarray(nums2, k - i)
            ans = max(ans, [max(arr1, arr2).pop(0) for _ in range(k)])
        return ans
