class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, count, pos):
            if len(cur) == count:
                ans.append(cur)
                return
            temp = nums[pos:]
            for i in range(len(temp)):
                dfs(cur + [temp[i]], count, pos + i + 1)

        nums.sort()
        ans = []
        for i in range(len(nums) + 1):
            dfs([], i, 0)
        return ans
