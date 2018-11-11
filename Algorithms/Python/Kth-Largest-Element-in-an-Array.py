class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random

        def getPivot(start, end):
            temp = random.randint(start, end)
            nums[end], nums[temp] = nums[temp], nums[end]
            idx, val = start, nums[end]
            for i in range(start, end):
                if nums[i] < val:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1
            nums[end], nums[idx] = nums[idx], nums[end]
            return idx

        def findKthSmallest(start, end, k):  # qselect
            if start <= end:
                pivot = getPivot(start, end)
                cur = (pivot - start) + 1
                if cur == k:
                    return nums[pivot]
                elif cur > k:
                    return findKthSmallest(start, pivot, k)
                else:
                    return findKthSmallest(pivot + 1, end, k - cur)

        return findKthSmallest(0, len(nums) - 1, len(nums) + 1 - k)
