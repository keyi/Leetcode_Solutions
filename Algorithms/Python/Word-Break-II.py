class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def check(word):
            if not word:
                return True

            arr = [False for i in range(len(word))]
            for i in range(len(word)):
                if word[:i + 1] in wordDict:
                    arr[i] = True
                    continue
                for j in range(i):
                    if arr[j] and word[j + 1:i + 1] in wordDict:
                        arr[i] = True
                        break
            return arr[-1]

        def dfs(cur, pos):
            if pos == len(s):
                ans.append(' '.join(cur))
                return
            temp = s[pos:]
            for i in range(len(temp)):
                x = temp[:i + 1]
                if x in wordDict:
                    dfs(cur + [x], pos + i + 1)

        ans = []
        if check(s):
            dfs([], 0)
        return ans
