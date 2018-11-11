class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        ans, flag = 0, False
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                ans, flag = mid + 1, True
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return ans if flag else start
