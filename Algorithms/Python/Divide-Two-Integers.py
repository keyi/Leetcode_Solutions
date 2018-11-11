class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        flag = True if divisor * dividend > 0 else False
        dvd, dvr, ans = abs(dividend), abs(divisor), 0
        while dvd >= dvr:
            count = 1
            temp = dvr
            while dvd >= temp + temp:
                temp += temp
                count += count
            dvd -= temp
            ans += count
        ans = ans if flag else 0 - ans
        if INT_MIN < ans and ans < INT_MAX:
            return ans
        elif ans <= INT_MIN:
            return INT_MIN
        else:
            return INT_MAX
