class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        ans = [triangle[0][0]]
        for i in range(1, len(triangle)):
            l, temp, cur = len(triangle[i]), 0, []
            for j in range(l):
                if j == 0:
                    temp = triangle[i][j] + ans[0]
                elif j == l - 1:
                    temp = triangle[i][j] + ans[-1]
                else:
                    temp = triangle[i][j] + min(ans[j - 1], ans[j])
                cur.append(temp)
            ans = cur
        return min(ans)
