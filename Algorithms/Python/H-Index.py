# Space O(1), Time O(NlgN)


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if i >= c:
                return i
        return len(citations)
