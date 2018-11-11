#  METHOD 1 Bit Manipulation


class Solution(object):

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans


# METHOD 2 String


class Solution(object):

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        s = '0' * (32 - len(s)) + s
        return int(s[::-1], 2)
