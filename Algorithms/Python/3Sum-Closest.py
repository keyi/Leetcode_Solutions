class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 2147483647
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if abs(total - target) < abs(ans - target):
                        ans = total
                    if total == target:
                        return target
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return ans
