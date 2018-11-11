class Stack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mystack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.mystack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.mystack) - 1):
            self.mystack.append(self.mystack.pop(0))
        self.mystack.pop(0)

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.mystack)):
            num = self.mystack.pop(0)
            self.mystack.append(num)
        return num

    def empty(self):
        """
        :rtype: bool
        """
        return self.mystack == []
