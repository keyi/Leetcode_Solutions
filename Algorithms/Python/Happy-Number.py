class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def cal(n):
            ans = 0
            while n != 0:
                ans += (n % 10)**2
                n //= 10
            return ans
        dic = {}
        while n not in dic:
            if n == 1:
                return True
            else:
                dic[n] = "add"
                n = cal(n)
        return False
