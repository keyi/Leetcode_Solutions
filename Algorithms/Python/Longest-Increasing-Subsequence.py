# METHOD 1: O(n*n)


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        s = [1] * l
        ans = 1
        for i in range(1, l):
            for j in range(i):
                if nums[j] < nums[i]:
                    s[i] = max(s[i], s[j] + 1)
            ans = max(ans, s[i])
        return ans

# METHOD 2: O(nlogn)


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(target):
            start, end = 0, len(ans) - 1
            while start <= end:
                mid = (start + end) // 2
                if ans[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            if start == len(ans):
                ans.append(target)
            else:
                ans[start] = target

        if not nums:
            return 0
        ans = []
        for x in nums:
            binarySearch(x)
        return len(ans)
