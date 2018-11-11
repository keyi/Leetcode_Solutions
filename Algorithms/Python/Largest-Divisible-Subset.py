class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        l = len(nums)
        dp, idx = [1] * l, [0] * l
        max_dp, max_idx = 1, -1
        ans = []
        for i in range(l):
            for j in reversed(range(i)):
                if nums[i] % nums[j] == 0 and dp[i] <= dp[j] + 1:
                    dp[i] = dp[j] + 1
                    idx[i] = j
            if max_dp < dp[i]:
                max_dp = dp[i]
                max_idx = i

        for i in range(max_dp):
            ans.append(nums[max_idx])
            max_idx = idx[max_idx]
        return ans
