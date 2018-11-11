class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, nums):
            if len(nums) == 1:
                ans.append(cur + nums)
                return
            pre, l = None, len(nums)
            for i in range(l):
                if nums[i] is not pre:
                    pre = nums[i]
                    dfs(cur + [nums[i]], nums[:i] + nums[i + 1:])

        ans = []
        nums.sort()
        dfs([], nums)
        return ans
