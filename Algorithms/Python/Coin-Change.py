class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = [0] + [-1] * amount
        for i in range(amount):
            if ans[i] != -1:
                for x in coins:
                    if (i + x <= amount) and (ans[i + x] == -1 or ans[i + x] > ans[i] + 1):
                        ans[i + x] = ans[i] + 1
        return ans[-1]
