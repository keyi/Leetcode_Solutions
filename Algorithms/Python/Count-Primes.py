class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n < 2:
            return 0
        arr = [True for x in range(n + 1)]
        for i in range(2, int(math.sqrt(n)) + 1):
            if arr[i]:
                for j in range(i**2, n + 1, i):
                    arr[j] = False
        return arr[2:n].count(True)
