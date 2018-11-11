class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        ans, k = '', k - 1
        fact = math.factorial(n - 1)
        nums = [x for x in range(1, n + 1)]
        for i in reversed(range(n)):
            cur = nums[k // fact]
            ans += str(cur)
            nums.remove(cur)
            if i > 0:
                k %= fact
                fact //= i
        return ans


# METHOD 2 (TLE)
# class Solution(object):

#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         def dfs(nums, cur, pos):
#             if not flag[0]:
#                 if len(nums) == 1:
#                     flag[2] += 1
#                     if flag[2] == flag[1]:
#                         flag[0] = True
#                         flag[2] = cur + nums[0]
#                     return
#                 for i in range(pos, len(nums)):
#                     dfs(nums[:i] + nums[i + 1:], cur + nums[i], 0)
#             else:
#                 return
#         import math
#         nums = [str(x) for x in range(1, n + 1)]
#         total = math.factorial(n)
#         pos = []
#         if total <= k:
#             return ''.join(nums[::-1])
#         else:
#             single = total / n
#             pos = k // single
#             k %= single
#         flag = [False, k, 0]
#         dfs(nums, '', pos)
#         return flag[2]
