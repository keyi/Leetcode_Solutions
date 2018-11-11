class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mystack = []
        self.mintemp = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.mystack.append(x)
        if not self.mintemp or self.mintemp[-1] >= x:
            self.mintemp.append(x)

    def pop(self):
        """
        :rtype: void
        """
        num = self.mystack.pop()
        if num == self.mintemp[-1]:
            self.mintemp.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mystack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mintemp[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
