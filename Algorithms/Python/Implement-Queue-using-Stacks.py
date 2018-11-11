class Queue(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myqueue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.myqueue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        for i in range(len(self.myqueue) - 1):
            temp.append(self.myqueue.pop())
        self.myqueue.pop()
        for i in range(len(temp)):
            self.myqueue.append(temp.pop())

    def peek(self):
        """
        :rtype: int
        """
        temp = []
        for i in range(len(self.myqueue)):
            num = self.myqueue.pop()
            temp.append(num)
        for i in range(len(temp)):
            self.myqueue.append(temp.pop())
        return num

    def empty(self):
        """
        :rtype: bool
        """
        return self.myqueue == []
