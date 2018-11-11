class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        import heapq
        s, ans = [], []
        counts = collections.Counter(nums)
        for key, cnt in counts.items():
            if len(s) < k:
                heapq.heappush(s, [cnt, key])
            else:
                if s[0][0] < cnt:
                    heapq.heappop(s)
                    heapq.heappush(s, [cnt, key])
        while s:
            ans.append(heapq.heappop(s)[1])
        return ans[::-1]
