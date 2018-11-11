class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        s = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                s[i] = s[i - 1] + 1
        for i in reversed(range(l - 1)):
            if ratings[i] > ratings[i + 1] and s[i] <= s[i + 1]:
                s[i] = s[i + 1] + 1
        return sum(s)
