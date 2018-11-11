class Solution(object):

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 3:
            return False
        t0, (t1, t2, t3) = 0, x[:3]
        bigger = True if t1 < t3 else False
        for i in range(3, len(x)):
            cur = x[i]
            if not bigger and cur >= t2:
                return True
            elif bigger and cur <= t2:
                if t0 + cur < t2 or (i + 1 < len(x) and x[i + 1] + t1 < t3):
                    bigger = False
                elif i + 1 < len(x):
                    return True
            t0, t1, t2, t3 = t1, t2, t3, cur
        return False
