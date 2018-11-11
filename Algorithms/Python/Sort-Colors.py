class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, index, end = 0, 0, len(nums) - 1
        while index <= end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            else:
                index += 1


# METHOD 2

class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for x in nums:
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1
        l = c0 + c1 + c2
        for i in range(l):
            if i < c0:
                nums[i] = 0
            elif i < c0 + c1:
                nums[i] = 1
            else:
                nums[i] = 2
