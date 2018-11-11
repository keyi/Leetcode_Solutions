class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(cur, num, pos):
            if num == target:
                if cur not in ans:
                    ans.append(cur)
                return
            else:
                temp = candidates[pos:]
                for i in range(len(temp)):
                    if num + temp[i] <= target:
                        dfs(cur + [temp[i]], num + temp[i], pos + i + 1)
                    else:
                        return
        ans = []
        candidates.sort()
        dfs([], 0, 0)
        return ans
