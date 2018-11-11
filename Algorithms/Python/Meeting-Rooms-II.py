# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Space O(N), Time O(NlgN)


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start, end = [], []
        for x in intervals:
            start.append(x.start)
            end.append(x.end)
        start.sort()
        end.sort()
        s, e = 0, 0
        ans, cnt = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                cnt += 1
                s += 1
                ans = max(ans, cnt)
            else:
                cnt -= 1
                e += 1
        return ans
