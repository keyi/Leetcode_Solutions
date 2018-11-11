class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s):
            return s == s[::-1]

        if not words:
            return []
        ans = []
        dic = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            # check reverse word
            if word[::-1] in dic and dic[word[::-1]] != i:
                ans.append([i, dic[word[::-1]]])

            # check empty word
            if '' in dic and word != '' and isPalindrome(word):
                ans.append([i, dic['']])
                ans.append([dic[''], i])

            for k in range(1, len(word)):
                left = word[:k]
                right = word[k:]
                # check prefix
                if isPalindrome(left) and right[::-1] in dic:
                    ans.append([dic[right[::-1]], i])
                # check postfix
                if isPalindrome(right) and left[::-1] in dic:
                    ans.append([i, dic[left[::-1]]])
        return ans
