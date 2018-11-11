class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def getExp(tokens):
            nums, ops, temp = [], [], 0
            for x in tokens:
                if x.isdigit():
                    temp = 10 * temp + int(x)
                else:
                    nums.append(temp)
                    ops.append(x)
                    temp = 0
            nums.append(temp)
            return nums, ops

        def cal(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            else:
                return num1 // num2

        def dac(nums, ops):
            if ops == []:
                return nums
            s = []
            for i in range(len(ops)):
                for l in dac(nums[:i + 1], ops[:i]):
                    for r in dac(nums[i + 1:], ops[i + 1:]):
                        s.append(cal(l, r, ops[i]))
            return s

        nums, ops = getExp(input)
        return dac(nums, ops)
