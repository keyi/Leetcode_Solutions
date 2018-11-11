class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def getBits(num):
            s = -1
            while num:
                s += 1
                num >>= 1
            return s

        if m == n or m == 0:
            return m
        bitm, bitn = getBits(m), getBits(n)
        ans = 0
        if bitm < bitn:
            return 0
        else:
            bit = bitm
            mark = (1 << bit)
            while (m & mark) == (n & mark):
                if m & mark == mark:
                    ans += mark
                    m -= mark
                    n -= mark
                    mark //= 2
                else:
                    mark //= 2
            return ans
