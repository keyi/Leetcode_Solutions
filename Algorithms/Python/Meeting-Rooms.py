# Definition for an interval.
# class Interval(object):

#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Space O(1), Time O(NlgN)


class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x.start)
        for i, x in enumerate(intervals[:-1]):
            if x.end > intervals[i + 1].start:
                return False
        return True
