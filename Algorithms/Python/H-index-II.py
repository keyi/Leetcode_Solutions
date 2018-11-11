# Space O(1), Time O(lgN)


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start, end, l = 0, len(citations), len(citations)
        while start < end:
            mid = (start + end) // 2
            if l - mid > citations[mid]:
                start = mid + 1
            else:
                end = mid
        return l - start
