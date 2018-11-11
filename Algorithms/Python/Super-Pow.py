class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        p = 0
        for x in b:
            p = p * 10 + x
        return (a ** p) % 1337
