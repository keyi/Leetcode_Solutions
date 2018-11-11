class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, minNum, maxNum = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            minTemp = minNum * x
            maxTemp = maxNum * x
            maxNum = max(max(minTemp, maxTemp), x)
            minNum = min(min(minTemp, maxTemp), x)
            if maxNum > ans:
                ans = maxNum
        return ans
