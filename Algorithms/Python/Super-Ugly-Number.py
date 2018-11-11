class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = [1]
        index = [0 for i in range(len(primes))]
        for i in range(1, n):
            val = [ans[index[j]] * primes[j] for j in range(len(primes))]
            num = min(val)
            for j in range(len(primes)):
                if num == val[j]:
                    index[j] += 1
            ans.append(num)
        return ans[-1]
