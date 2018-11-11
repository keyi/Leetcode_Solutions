class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in dic:
                for x in dic[nums[i]]:
                    if i - x <= k:
                        return True
            dic[nums[i]].append(i)
        return False
