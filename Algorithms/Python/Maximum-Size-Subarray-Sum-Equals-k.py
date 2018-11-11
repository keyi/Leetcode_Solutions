# Space O(N), Time O(N)


class Solution(object):

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val, maxLen, dic = 0, 0, {}
        for i, x in enumerate(nums):
            val += x
            if val == k:
                maxLen = i + 1
            elif (val - k) in dic:
                maxLen = max(maxLen, i - dic[val - k])
            if val not in dic:
                dic[val] = i
        return maxLen
