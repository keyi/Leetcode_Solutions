class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = []
        candidate1, candidate2 = nums[0] - 1, nums[0] - 1
        count1, count2 = 0, 0
        for x in nums:
            if x == candidate1:
                count1 += 1
            elif x == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = x
                count1 = 1
            elif count2 == 0:
                candidate2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2, l = 0, 0, len(nums)
        for x in nums:
            if x == candidate1:
                count1 += 1
            elif x == candidate2:
                count2 += 1
        if count1 > l // 3:
            ans.append(candidate1)
        if count2 > l // 3:
            ans.append(candidate2)
        return ans
