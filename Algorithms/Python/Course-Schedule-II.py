class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        import collections
        zero_degree, in_degree, out_degree = collections.deque(), collections.defaultdict(
            set), collections.defaultdict(set)
        for i, j in prerequisites:
            in_degree[i].add(j)
            out_degree[j].add(i)

        for i in range(numCourses):
            if i not in in_degree:
                zero_degree.append(i)

        while zero_degree:
            course = zero_degree.popleft()
            ans.append(course)
            if course in out_degree:
                for x in out_degree[course]:
                    in_degree[x].discard(course)
                    if not in_degree[x]:
                        zero_degree.append(x)
                del out_degree[course]

        return [] if out_degree else ans
