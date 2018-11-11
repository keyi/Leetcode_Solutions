class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, dic):
            if len(cur) == l:
                ans.append(cur)
                return
            else:
                for i in range(l):
                    if i not in dic or not dic[i]:
                        dic[i] = True
                        dfs(cur + [nums[i]], dic)
                        dic[i] = False
        ans, l = [], len(nums)
        dfs([], {})
        return ans


# METHOD 2
class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, nums):
            if len(nums) == 1:
                ans.append(cur + nums)
                return
            l = len(nums)
            for i in range(l):
                dfs(cur + [nums[i]], nums[:i] + nums[i + 1:])

        ans = []
        dfs([], nums)
        return ans
