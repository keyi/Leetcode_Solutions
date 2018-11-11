class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        for x in nums:
            s ^= x
        temp = 1
        while s & temp == 0:
            temp <<= 1
        first, second = 0, 0
        for x in nums:
            if x & temp == 0:
                first ^= x
            else:
                second ^= x
        return [first, second]
