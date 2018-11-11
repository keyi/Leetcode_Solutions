class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from itertools import combinations

        def getHour(n):
            if n == 0:
                return ['0']
            s = []
            arr = combinations([1, 2, 4, 8], n)
            for i in arr:
                temp = sum(i)
                if temp < 12:
                    s.append(str(temp))
            return s

        def getMinute(n):
            if n == 0:
                return ['00']
            s = []
            arr = combinations([1, 2, 4, 8, 16, 32], n)
            for i in arr:
                temp = sum(i)
                if temp < 60:
                    if temp >= 10:
                        s.append(str(temp))
                    else:
                        s.append('0' + str(temp))
            return s

        ans = []
        for i in range(num + 1):
            temp = []
            hour = getHour(i)
            minute = getMinute(num - i)
            for h in hour:
                for m in minute:
                    temp.append(h + ":" + m)
            ans.extend(temp)
        return ans

# Method 2


class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    s = "%d:%02d" % (h, m)
                    ans.append(s)
        return ans
