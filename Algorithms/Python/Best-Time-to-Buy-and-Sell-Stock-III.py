class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        l = len(prices)
        lowest = prices[0]
        sell = [0] * l
        for i in range(1, l):
            lowest = min(lowest, prices[i])
            sell[i] = max(sell[i - 1], prices[i] - lowest)

        highest = prices[-1]
        buy = [0] * l
        for i in range(l - 2, -1, -1):
            highest = max(highest, prices[i])
            buy[i] = max(buy[i + 1], highest - prices[i])

        ans = 0
        for i in range(l):
            ans = max(ans, sell[i] + buy[i])
        return ans
