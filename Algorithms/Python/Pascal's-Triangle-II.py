class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex + 1):
            temp = ans
            ans = [1] * (rowIndex + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    pass
                else:
                    ans[j] = temp[j - 1] + temp[j]
        return ans
