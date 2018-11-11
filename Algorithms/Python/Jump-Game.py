class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        cur = 1
        for i in range(len(nums)):
            cur -= 1
            if cur < 0:
                return False
            else:
                cur = max(cur, nums[i])
            if cur >= l - 1 - i:
                return True
        return False
