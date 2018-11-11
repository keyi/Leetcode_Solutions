class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return l
        slow, fast = 0, 1
        pre = 'flag'
        while fast < l:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            elif nums[fast] != pre:
                slow += 1
                nums[slow] = nums[fast]
                pre = nums[fast]
            fast += 1
        return slow + 1
