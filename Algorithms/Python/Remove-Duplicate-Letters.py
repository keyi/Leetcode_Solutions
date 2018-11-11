class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans, vis, cnt = [], [False] * 26, [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        for c in s:
            idx = ord(c) - 97
            cnt[idx] -= 1
            if vis[idx]:
                continue
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - 97] > 0:
                vis[ord(ans.pop()) - 97] = False
            ans.append(c)
            vis[idx] = True
        return ''.join(ans)
