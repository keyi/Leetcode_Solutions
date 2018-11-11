class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        A, B, l = min(nums), max(nums), len(nums)
        if A == B:
            return 0
        bucketSize = max(1, (B - A) // (l - 1))
        bucketNum = (B - A) // bucketSize + 1
        bucket = [None] * bucketNum
        for x in nums:
            idx = (x - A) // bucketSize
            if not bucket[idx]:
                bucket[idx] = {'max': x, 'min': x}
            else:
                bucket[idx]['max'] = max(x, bucket[idx]['max'])
                bucket[idx]['min'] = min(x, bucket[idx]['min'])

        ans, i = 0, 0
        while i < bucketNum:
            if not bucket[i]:
                i += 1
            else:
                j = i + 1
                while j < bucketNum and not bucket[j]:
                    j += 1
                if j < bucketNum:
                    ans = max(ans, bucket[j]['min'] - bucket[i]['max'])
                i = j
        return ans
