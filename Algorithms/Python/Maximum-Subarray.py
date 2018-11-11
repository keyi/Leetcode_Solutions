class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, temp = nums[0], nums[0]
        for x in nums[1:]:
            if temp < 0:
                if x >= 0:
                    temp = x
            else:
                temp += x
            ans = max([ans, temp, x])
        return ans
