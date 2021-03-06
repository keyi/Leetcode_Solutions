class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i // 2] + 1 if i % 2 else ans[i // 2]
        return ans
