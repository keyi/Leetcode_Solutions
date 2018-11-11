# Time(O(N))


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        import collections
        ans, dq = [], collections.deque()
        for i in range(len(nums)):   # window: [i-(k-1),i]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            while dq and dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
