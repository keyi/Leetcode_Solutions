# Definition for a point.
# class Point(object):

#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        ans = 1
        for i in range(len(points) - 1):
            start = points[i]
            samepoint = 1
            dic = {'inf': 0}
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    samepoint += 1
                elif start.x == end.x:
                    dic['inf'] += 1
                else:
                    ydiff = start.y - end.y
                    xdiff = start.x - end.x
                    slope = float(ydiff) / xdiff
                    if slope in dic:
                        dic[slope] += 1
                    else:
                        dic[slope] = 1
            ans = max(ans, max(dic.values()) + samepoint)
        return ans
