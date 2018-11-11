class Solution:
    # @param {integer[]} nums
    # @return {string}

    def largestNumber(self, nums):
        def compare(a, b):
            return [1, -1][a + b > b + a]
        nums = [str(x) for x in nums]
        nums.sort(cmp=compare)
        ans = ''.join(nums).lstrip('0')
        return [ans, '0'][not ans]
