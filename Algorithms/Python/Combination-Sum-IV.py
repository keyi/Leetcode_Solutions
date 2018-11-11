class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    dp[i] += dp[i - x]
        return dp[-1]
