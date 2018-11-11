class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        num, ans = 0, []
        for x in digits:
            num = num * 10 + x
        num += 1
        while num != 0:
            ans.insert(0, num % 10)
            num //= 10
        return ans
