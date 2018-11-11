class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i, l = 0, len(nums)
        while i < l:
            if 0 < nums[i] <= l and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1
