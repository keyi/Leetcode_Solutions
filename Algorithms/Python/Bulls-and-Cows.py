class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import collections
        bulls, cows, dic = 0, 0, collections.defaultdict(int)
        for i in range(len(secret)):
            temp = secret[i]
            if temp == guess[i]:
                bulls += 1
            else:
                dic[temp] += 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in dic and dic[guess[i]] > 0:
                cows += 1
                dic[guess[i]] -= 1
        return '%dA%dB' % (bulls, cows)
