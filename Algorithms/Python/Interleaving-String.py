class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        ans = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        ans[0][0] = True
        for i in range(1, l1 + 1):
            ans[i][0] = ans[i - 1][0] and (s1[i - 1] == s3[i - 1])
        for j in range(1, l2 + 1):
            ans[0][j] = ans[0][j - 1] and (s2[j - 1] == s3[j - 1])
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                ans[i][j] = (ans[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                             ) or (ans[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return ans[-1][-1]
