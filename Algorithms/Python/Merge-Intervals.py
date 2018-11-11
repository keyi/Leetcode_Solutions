# Definition for an interval.
# class Interval(object):

#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = []
        for i in range(len(intervals) - 1):
            if intervals[i].end < intervals[i + 1].start:
                ans.append(intervals[i])
            else:
                intervals[i + 1].start = intervals[i].start
                intervals[
                    i + 1].end = max(intervals[i].end, intervals[i + 1].end)
        ans.append(intervals[-1])
        return ans
