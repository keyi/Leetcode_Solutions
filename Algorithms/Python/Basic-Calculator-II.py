# input string: int, '+', '-', '*' and '/'


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def getExp(tokens):  # get Infix Notation from input string
            tokens = tokens.replace(' ', '')
            ans, temp = [], ""
            for x in tokens:
                if x.isdigit():
                    temp += x
                else:
                    ans.extend([temp, x])
                    temp = ""
            ans.append(temp)
            return ans

        def convertExp(tokens):  # convert Infix Notation to Postfix Notation
            ans, stack = [], []
            for x in tokens:
                if x.isdigit():
                    ans.append(x)
                else:
                    while stack and dic[stack[-1]] >= dic[x]:
                        ans.append(stack.pop())
                    stack.append(x)
            ans.extend(stack[::-1])
            return ans

        def interpreteExp(tokens):  # get output from Postfix Notation
            stack = []
            for x in tokens:
                if x.isdigit():
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
                        stack.append(a / b)
            return stack[0]

        dic = {'+': 1, '-': 1, '*': 2, '/': 2}
        s = getExp(s)
        s = convertExp(s)
        s = interpreteExp(s)
        return s
