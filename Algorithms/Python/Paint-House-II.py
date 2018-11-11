# Space O(K), Time O(N * K)


class Solution(object):

    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min([costs[i - 1][k]
                                    for k in range(len(costs[0])) if k != j])
        return min(costs[-1])
