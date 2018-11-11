class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        start, end = nums[0], nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                end = nums[i + 1]
            else:
                cur = str(start) if start == end else str(
                    start) + '->' + str(end)
                ans.append(cur)
                start, end = nums[i + 1], nums[i + 1]
            i += 1
        cur = str(start) if start == end else str(start) + '->' + str(end)
        ans.append(cur)
        return ans
