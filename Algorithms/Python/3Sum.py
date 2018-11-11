class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == 0:
                        cur = [nums[i], nums[left], nums[right]]
                        ans.append(cur)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total > 0:
                        right -= 1
                    else:
                        left += 1
        return ans


# METHOD 2


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, dic, l, = [], {}, len(nums)
        nums.sort()
        for i in range(l):
            x = nums[i]
            if x in dic:
                dic[x].append(i)
            else:
                dic[x] = [i]

        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                s1, s2 = nums[i], nums[j]
                x = 0 - s1 - s2
                if x in dic:
                    for k in dic[x][::-1]:
                        if k > j:
                            if [s1, s2, x] not in ans:
                                ans.append([s1, s2, x])
                            break
        return ans
