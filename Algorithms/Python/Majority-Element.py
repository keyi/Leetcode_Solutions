class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    index, count = i, 1
        return nums[index]

# METHOND 2


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
            if dic[x] > len(nums) // 2:
                return x
