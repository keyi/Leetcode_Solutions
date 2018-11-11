class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        ans = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1 + 1):
            ans[i][0] = i
        for j in range(l2 + 1):
            ans[0][j] = j

        for i in range(l1):
            for j in range(l2):
                insert = ans[i + 1][j] + 1
                delete = ans[i][j + 1] + 1
                replace = ans[i][j] + \
                    (0 if word1[i] == word2[j] else 1)
                ans[i + 1][j + 1] = min(ans, insert, delete, replace)
        return ans[-1][-1]
