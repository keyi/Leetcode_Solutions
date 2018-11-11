class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(cur, num, count, pos):
            if num == n and count == k:
                ans.append(cur)
                return
            else:
                temp = s[pos:]
                for i in range(len(temp)):
                    if num + temp[i] <= n:
                        dfs(cur + [temp[i]], num + temp[i],
                            count + 1, pos + i + 1)
                    else:
                        return

        s = [x for x in range(1, 10)]
        ans = []
        dfs([], 0, 0, 0)
        return ans
