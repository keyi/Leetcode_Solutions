# Space O(1), Time O(N)


class Solution(object):

    import random

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.rd = random

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans = -1
        cnt = 0
        for i, x in enumerate(self.nums):
            if x != target:
                continue
            cnt += 1
            if self.rd.randint(1, cnt) == 1:
                ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
