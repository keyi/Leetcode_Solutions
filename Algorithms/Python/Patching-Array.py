class Solution(object):

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        import math
        if not nums:
            return int(math.log(n, 2)) + 1
        ans = 0
        index, cur = 0, 1
        while cur <= n:
            if index < len(nums) and nums[index] <= cur:
                cur += nums[index]
                index += 1
            else:
                ans += 1
                cur <<= 1
        return ans
