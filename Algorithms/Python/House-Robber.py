class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) < 3:
            return max(nums)
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for x in nums[2:]:
            nex = max(cur, pre + x)
            pre, cur = cur, nex
        return cur
