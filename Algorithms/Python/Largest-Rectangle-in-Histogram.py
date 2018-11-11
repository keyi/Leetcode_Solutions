class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
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
                    ans = max(ans, h * (i - index))
                stack.append([index, height])
        while stack:
            last = stack.pop()
            index = last[0]
            h = last[1]
            ans = max(ans, h * (len(heights) - index))
        return ans
