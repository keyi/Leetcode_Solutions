class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] == 0:
                fast += 1
                continue
            elif nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
