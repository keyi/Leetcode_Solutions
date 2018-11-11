#  METHOD 1 Bit Manipulation


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >= 1 and n & (n - 1) == 0

#  METHOD 2 String


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        s = bin(n)[2:]
        return s.count('1') == 1

#  METHOD 3 Math


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        return False if n <= 0 else n == 2**round(math.log(n, 2))
