class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = [int(x) for x in num1[::-1]], [int(x) for x in num2[::-1]]
        l1, l2 = len(num1), len(num2)
        l = l1 + l2
        s = [0] * l
        for i in range(l1):
            div = 0
            for j in range(l2):
                cur = num1[i] * num2[j] + div
                div, remain = cur // 10, cur % 10
                s[i + j] += remain
            if div:
                s[i + j + 1] = div
        ans, div = 0, 0
        for i in range(l):
            ans = 10**i * s[i] + ans
        return str(ans)
