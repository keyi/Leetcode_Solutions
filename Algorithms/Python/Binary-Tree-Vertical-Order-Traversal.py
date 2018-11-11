# Space O(N), Time O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        if not root:
            return []
        queue = collections.deque([(0, root)])
        dic = collections.defaultdict(list)
        while queue:
            i, node = queue.popleft()
            if node:
                dic[i].append(node.val)
                queue += (i - 1, node.left), (i + 1, node.right)
        ans = [dic[i] for i in range(min(dic.keys()), max(dic.keys()) + 1)]
        return ans
