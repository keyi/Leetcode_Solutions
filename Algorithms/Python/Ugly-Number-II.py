class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n - 1):
            m2, m3, m5 = 2 * ans[i2], 3 * ans[i3], 5 * ans[i5]
            temp = min(m2, m3, m5)
            if temp == m2:
                i2 += 1
            if temp == m3:
                i3 += 1
            if temp == m5:
                i5 += 1
            ans.append(temp)
        return ans[-1]
