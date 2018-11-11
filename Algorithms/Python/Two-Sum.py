class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic[temp], i]
            else:
                dic[nums[i]] = i
