class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        ans = [[beginWord, 1]]
        chars = [chr(x) for x in range(97, 123)]
        while ans:
            cur = ans.pop(0)
            curword, curlen = cur[0], cur[1]
            if curword == endWord:
                return curlen
            for i in range(len(curword)):
                for x in chars:
                    if curword[i] != x:
                        candidate = curword[:i] + x + curword[i + 1:]
                        if candidate in wordList:
                            if candidate == endWord:
                                return curlen + 1
                            else:
                                ans.append([candidate, curlen + 1])
                                wordList.remove(candidate)
        return 0
