# METHOD 1  Time: O(n), Space: O(1)


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        self.rev(nums, 0, l - k)
        self.rev(nums, l - k, l)
        self.rev(nums, 0, l)

    def rev(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

# METHOD 2  Time: O(n*(k%n)), Space: O(1)


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        for i in range(k):
            temp = nums[-1]
            for j in range(l - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = temp

# METHOD 3  Time: O(n), Space: O(n)


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        s = nums[l - k:] + nums[:l - k]
        for i in range(len(s)):
            nums[i] = s[i]
