class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mydata = []
        self.length = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.mydata:
            self.mydata.append(num)
        else:
            flag = True
            for i in range(self.length):
                if self.mydata[i] >= num:
                    self.mydata.insert(i, num)
                    flag = False
                    break
            if flag:
                self.mydata.append(num)
        self.length += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.length % 2 == 0:
            return float(self.mydata[self.length // 2 - 1] +
                         self.mydata[self.length // 2]) / 2
        else:
            return float(self.mydata[self.length // 2])
