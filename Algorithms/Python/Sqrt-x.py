class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        start, end = 1, x
        while start < end:
            mid = (start + end) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                end = mid
            else:
                start = mid
            if start == end - 1:
                break
        return start
