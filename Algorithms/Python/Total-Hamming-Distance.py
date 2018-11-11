class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            mark = 1 << i
            zero, one = 0, 0
            for x in nums:
                if x & mark:
                    one += 1
                else:
                    zero += 1
            ans += one * zero
        return ans
