class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if int(math.sqrt(n)) ** 2 == n:
            return 1
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        i = 1
        while i * i <= n:
            j = int(math.sqrt(n - i * i))
            if i * i + j * j == n:
                return 2
            i += 1
        return 3
