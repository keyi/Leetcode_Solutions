class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def daq(i, j):
            if ans[i][j] > 0:
                return ans[i][j]
            for x in range(i, j + 1):
                ans[i][j] = max(ans[i][j], daq(i, x - 1) + nums[i - 1] *
                                nums[x] * nums[j + 1] + daq(x + 1, j))
            return ans[i][j]

        l = len(nums)
        nums = [1] + nums + [1]
        ans = [[0 for _ in range(l + 2)] for _ in range(l + 2)]
        daq(1, l)
        return ans[1][l]
