class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = -1, -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                left = i
        if left == -1:
            nums.reverse()
            return

        for i in range(left + 1, len(nums)):
            if nums[i] > nums[left]:
                right = i
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1:] = nums[:left: -1]
