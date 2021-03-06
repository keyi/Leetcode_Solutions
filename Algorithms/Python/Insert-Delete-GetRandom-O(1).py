class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        idx = self.dic[val]
        last = self.arr[-1]
        self.dic[last], self.arr[idx] = idx, last
        self.arr.pop()
        del self.dic[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        idx = random.randint(1, len(self.arr))
        return self.arr[idx - 1]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
