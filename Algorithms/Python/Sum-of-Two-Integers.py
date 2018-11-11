class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans, flag = [], 0
        a = [int(x) for x in bin(a)[2:]]
        b = [int(x) for x in bin(b)[2:]]
        la, lb = len(a), len(b)
        if la < lb:
            a = (lb - la) * [0] + a
        elif la > lb:
            b = (la - lb) * [0] + b
        while a and b:
            aa, bb = a.pop(), b.pop()
            if aa == 0 and bb == 0:
                cur = flag
                flag = 0
            elif aa & bb == 1:
                cur = flag
                flag = 1
            else:
                cur = 1 ^ flag
            ans.insert(0, str(cur))
        if flag:
            ans.insert(0, str(flag))
        return int(''.join(ans), 2)
