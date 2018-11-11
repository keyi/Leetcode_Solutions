class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(cur, num, pos):
            if num == target:
                ans.append(cur)
                return
            else:
                temp = candidates[pos:]
                for i in range(len(temp)):
                    if num + temp[i] <= target:
                        dfs(cur + [temp[i]], num + temp[i], pos + i)
                    else:
                        return
        ans = []
        candidates.sort()
        dfs([], 0, 0)
        return ans
