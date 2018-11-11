class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length, total = 0, 0
        for x in nums:
            length += 1
            total += x
        return (0 + length + 1) * (length) // 2 - total
