class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        left, right = -1, -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                count, temp = -1, mid
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                    count += 1
                left, mid = mid + 1, temp + 1
                while mid < len(nums) and nums[mid] == target:
                    count += 1
                    mid += 1
                right = left + count
                break
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [left, right]
