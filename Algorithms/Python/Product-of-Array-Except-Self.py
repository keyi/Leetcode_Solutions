class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        temp = 1
        for x in nums:
            ans.append(temp)
            temp *= x
        temp = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * temp
            temp *= nums[i]
        return ans
