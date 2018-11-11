class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        count, ans = 0, ''
        begin, minLen = 0, 2147483647
        need, found = collections.defaultdict(int), {}

        for x in t:
            need[x] += 1
            found[x] = 0
        for i, x in enumerate(s):
            if x in need:
                found[x] += 1
                if found[x] <= need[x]:
                    count += 1
            if count >= len(t):
                temp = s[begin]
                while (temp not in found) or found[temp] > need[temp]:
                    begin += 1
                    if temp in found:
                        found[temp] -= 1
                    temp = s[begin]
                if i + 1 - begin < minLen:
                    minLen = i + 1 - begin
                    ans = s[begin:i + 1]
        return ans
