class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        ans = (C - A) * (D - B) + (G - E) * (H - F)
        if A > G or C < E or B > H or D < F:
            return ans
        else:
            overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
            return ans - overlap
