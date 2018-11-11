class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getNum(s):
            pre, cur = s[0], max(s[0], s[1])
            for x in s[2:]:
                nex = pre + x
                pre = cur
                cur = max(nex, cur)
            return cur

        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        return max(getNum(nums[:-1]), getNum(nums[1:]))
