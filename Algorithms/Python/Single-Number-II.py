class Solution:
    # @param {integer[]} A
    # @return {integer}

    def singleNumber(self, nums):
        ans, flag = 0, 1
        for i in range(32):
            count, temp = 0, 0
            for x in nums:
                if x < 0:
                    temp += 1
                    x = -x
                if (x >> i) & 1 == 1:
                    count += 1
            flag = 1 if temp % 3 == 0 else -1
            count %= 3
            ans |= (count << i)
        return ans * flag
