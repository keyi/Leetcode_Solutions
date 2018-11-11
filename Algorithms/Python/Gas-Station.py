class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        diff = [gas[i] - cost[i] for i in range(l)]
        if sum(diff) < 0:
            return -1
        index, total = 0, 0
        for i in range(l):
            if total + diff[i] < 0:
                total = 0
                index = i + 1
            else:
                total += diff[i]
        return index if index < l else -1
