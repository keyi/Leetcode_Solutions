class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans, dic = [], {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                x = nums[i] + nums[j]
                if x not in dic:
                    dic[x] = [[i, j]]
                else:
                    dic[x].append([i, j])
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        x = target - nums[i] - nums[j]
                        if x in dic:
                            for temp in dic[x]:
                                if temp[0] > j:
                                    cur = [nums[i], nums[j], nums[
                                        temp[0]], nums[temp[1]]]
                                    if cur not in ans:
                                        ans.append(cur)
        return ans


# METHOD 2

class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        left, right = j + 1, len(nums) - 1
                        while left < right:
                            total = nums[i] + nums[j] + \
                                nums[left] + nums[right]
                            if total == target:
                                cur = [nums[i], nums[j],
                                       nums[left], nums[right]]
                                ans.append(cur)
                                left += 1
                                right -= 1
                                while left < right and nums[left] == nums[left - 1]:
                                    left += 1
                                while left < right and nums[right] == nums[right + 1]:
                                    right -= 1
                            elif total < target:
                                left += 1
                            else:
                                right -= 1
        return ans
