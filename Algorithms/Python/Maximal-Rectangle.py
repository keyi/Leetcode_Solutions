class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            s = 0
            stack = []
            for i, height in enumerate(heights):
                if stack == [] or height >= stack[-1][1]:
                    stack.append([i, height])
                else:
                    index = 0
                    while stack and height < stack[-1][1]:
                        last = stack.pop()
                        index = last[0]
                        h = last[1]
                        s = max(s, h * (i - index))
                    stack.append([index, height])
            while stack:
                last = stack.pop()
                index = last[0]
                h = last[1]
                s = max(s, h * (len(heights) - index))
            return s

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0:
                    heights[j] = int(matrix[i][j])
                else:
                    heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            ans = max(ans, largestRectangleArea(heights))
        return ans
