# Definition for an interval.
# class Interval(object):

#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def mergeIntervals(intervals):
            intervals.sort(key=lambda x: x.start)
            s = []
            for i in range(len(intervals) - 1):
                if intervals[i].end < intervals[i + 1].start:
                    s.append(intervals[i])
                else:
                    intervals[i + 1].start = intervals[i].start
                    intervals[
                        i + 1].end = max(intervals[i].end, intervals[i + 1].end)
            s.append(intervals[-1])
            return s

        if not intervals:
            return [newInterval]
        if newInterval.start <= intervals[0].start:
            intervals.insert(0, newInterval)
        elif newInterval.start >= intervals[-1].start:
            intervals.append(newInterval)
        else:
            for i in range(len(intervals) - 1):
                if intervals[i].start <= newInterval.start <= intervals[i + 1].start:
                    intervals.insert(i + 1, newInterval)
                    break

        return mergeIntervals(intervals)
