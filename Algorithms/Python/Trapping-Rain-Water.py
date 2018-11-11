# METHOD 1


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        l = len(height)
        left = [0] * l
        left[0] = height[0]
        for i in range(1, l):
            left[i] = max(left[i - 1], height[i])
        right = [0] * l
        right[-1] = height[-1]
        for i in range(l - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        return sum([max(0, min(left[i], right[i]) - height[i])
                    for i in range(l)])

# METHOD 2


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        ans = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[0], height[-1]
        while left <= right:
            level = min(maxLeft, maxRight)
            if maxLeft <= maxRight:
                ans += max(0, level - height[left])
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                ans += max(0, level - height[right])
                maxRight = max(maxRight, height[right])
                right -= 1

        return ans
