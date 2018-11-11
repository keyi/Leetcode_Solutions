class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        slow, fast = 0, len(height) - 1
        ans = 0
        while slow < fast:
            ans = max(ans, (fast - slow) * min(height[fast], height[slow]))
            if height[slow] < height[fast]:
                slow += 1
            elif height[slow] > height[fast]:
                fast -= 1
            else:
                slow += 1
                fast -= 1
        return ans
