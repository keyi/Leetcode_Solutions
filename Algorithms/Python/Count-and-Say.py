class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n - 1):
            temp, pre = '', s[0]
            count = 1
            for x in s[1:]:
                if x == pre:
                    count += 1
                else:
                    temp += (str(count) + pre)
                    count, pre = 1, x
            temp += (str(count) + pre)
            s = temp
        return s
