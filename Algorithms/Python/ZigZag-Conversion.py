class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = [''] * numRows
        row, flag = 0, True  # True for down, False for up
        for i in range(len(s)):
            ans[row] += s[i]
            if row == 0:
                flag = True
            elif row == numRows - 1:
                flag = False
            row = row + 1 if flag else row - 1
        return ''.join(ans)
