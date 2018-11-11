class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        ans = 2147483647
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                ans = min(ans, i - start + 1)
                total -= nums[start]
                start += 1
        return 0 if ans == 2147483647 else ans
