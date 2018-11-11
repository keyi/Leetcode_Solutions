class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if x.isdigit() or x[1:].isdigit():
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x == '+':
                    stack.append(a + b)
                elif x == '-':
                    stack.append(a - b)
                elif x == '*':
                    stack.append(a * b)
                else:
                    flag = 1 if a * b > 0 else -1
                    temp = abs(a) // abs(b)
                    stack.append(flag * temp)
        return stack[0]
