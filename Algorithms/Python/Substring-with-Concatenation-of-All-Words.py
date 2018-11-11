class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections
        dic = collections.defaultdict(int)
        for x in words:
            dic[x] += 1
        ans = []
        num, length = len(words), len(words[0])
        for i in range(len(s) + 1 - num * length):
            j = 0
            cur = collections.defaultdict(int)
            while j < num:
                x = s[i + j * length:i + (j + 1) * length]
                if x not in dic:
                    break
                cur[x] += 1
                if cur[x] > dic[x]:
                    break
                else:
                    j += 1
            if j == num:
                ans.append(i)
        return ans
