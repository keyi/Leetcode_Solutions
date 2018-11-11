class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        m, n = len(dungeon), len(dungeon[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        ans[-1][-1] = max(0, 0 - dungeon[-1][-1])
        for i in reversed(range(m - 1)):
            ans[i][-1] = max(0, ans[i + 1][-1] - dungeon[i][-1])
        for j in reversed(range(n - 1)):
            ans[-1][j] = max(0, ans[-1][j + 1] - dungeon[-1][j])
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                ans[i][j] = max(
                    0, min(ans[i][j + 1], ans[i + 1][j]) - dungeon[i][j])
        return ans[0][0] + 1
