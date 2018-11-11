# METHOD 1 Bit Manipulation


class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) < 2:
            return 0
        bits = [0] * len(words)

        for i, word in enumerate(words):
            for c in set(word):
                bits[i] |= (1 << (ord(c) - ord('a')))

        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if bits[i] & bits[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

# METHOD 2 Bit Manipulation + Sort


class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) < 2:
            return 0

        words.sort(key=lambda x: len(x), reverse=True)
        bits = [0] * len(words)
        for i, word in enumerate(words):
            for c in set(word):
                bits[i] |= (1 << (ord(c) - ord('a')))

        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                cur = len(words[i]) * len(words[j])
                if cur <= ans:
                    break
                elif bits[i] & bits[j] == 0:
                    ans = cur

        return ans


# METHOD 3 (TLE)


# class Solution(object):

#     def maxProduct(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         def getLength(w1, w2):
#             dic = {}
#             for x in w1:
#                 if x not in dic:
#                     dic[x] = True
#             for x in w2:
#                 if x in dic:
#                     return 0
#             return len(w1) * len(w2)

#         ans = 0
#         for i in range(len(words) - 1):
#             for j in range(i + 1, len(words)):
#                 ans = max(ans, getLength(words[i], words[j]))
#         return ans
