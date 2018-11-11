class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def binarySearch(target):
            start, end = 0, len(ans) - 1
            while start <= end:
                mid = (start + end) // 2
                if ans[mid][1] < target[1]:
                    start = mid + 1
                else:
                    end = mid - 1
            if start == len(ans):
                ans.append(target)
            else:
                ans[start] = target

        envelopes.sort(cmp=lambda x, y: x[
                       0] - y[0] if x[0] != y[0] else y[1] - x[1])
        ans = []
        for x in envelopes:
            binarySearch(x)
        return len(ans)
