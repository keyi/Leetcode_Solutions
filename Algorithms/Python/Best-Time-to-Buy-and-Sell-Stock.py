class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        ans, minNum = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minNum:
                ans = max(prices[i] - minNum, ans)
            else:
                minNum = prices[i]
        return ans
