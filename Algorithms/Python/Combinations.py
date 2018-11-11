class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(cur, k, pos):
            if len(cur) == k:
                ans.append(cur)
                return
            temp = nums[pos:]
            for i in range(len(temp)):
                dfs(cur + [temp[i]], k, pos + i + 1)

        if n < k:
            return []
        nums = [x for x in range(1, n + 1)]
        ans = []
        dfs([], k, 0)
        return ans
