class Solution(object):

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def bfs(beginWord, endWord, wordlist):
            found = False
            cur, visited = [beginWord], set()
            while cur and not found:
                nex = set()
                for x in cur:
                    visited.add(x)
                for word in cur:
                    for i in range(len(word)):
                        for x in chars:
                            if word[i] != x:
                                candidate = word[
                                    :i] + x + word[i + 1:]
                                if candidate in wordlist and candidate not in visited:
                                    if candidate == endWord:
                                        found = True
                                    nex.add(candidate)
                                    trace[candidate].append(word)

                cur = nex

        def dfs(cur, end):
            if end == beginWord:
                ans.append(cur)
                return
            for x in trace[end]:
                dfs([x] + cur, x)

        ans = []
        wordlist.add(endWord)
        trace = {word: [] for word in wordlist}
        chars = [chr(x) for x in range(97, 123)]
        bfs(beginWord, endWord, wordlist)
        dfs([endWord], endWord)
        return ans
