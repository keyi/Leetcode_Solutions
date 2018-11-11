class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    pass
                else:
                    temp[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(temp)
        return ans
