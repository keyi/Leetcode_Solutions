class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[mid] >= nums[right]:
                left = mid
            else:
                right = mid
            if left + 1 == right:
                return min(nums[left], nums[right])

# METHOD 2


class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        left = 0
        right = len(num) - 1
        while left <= right:
            mid = (left + right) // 2
            if num[mid] < num[right]:
                right = mid
            elif num[left] < num[mid]:
                left = mid
            else:
                left += 1
        return num[left - 1]
