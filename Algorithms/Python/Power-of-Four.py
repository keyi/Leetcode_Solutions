#  METHOD 1 Bit Manipulation


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = int('0b' + '01' * 16, 2)
        return num >= 1 and num & (num - 1) == 0 and num & flag == num

# METHOD 2 String


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = bin(num)[2:]
        return s[0] == '1' and s.count('1') == 1 and s.count('0') % 2 == 0
