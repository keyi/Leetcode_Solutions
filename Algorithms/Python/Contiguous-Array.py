# Space O(N), Time O(N)


class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic, cnt, ans = {0: 0}, 0, 0
        for i, x in enumerate(nums, 1):
            cnt = cnt + 1 if x == 1 else cnt - 1
            if cnt in dic:
                ans = max(ans, i - dic[cnt])
            else:
                dic[cnt] = i
        return ans
