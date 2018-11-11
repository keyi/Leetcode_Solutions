# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0, 0
            robL, no_robL = dfs(node.left)
            robR, no_robR = dfs(node.right)
            return node.val + no_robL + no_robR, max(robL, no_robL) + max(robR, no_robR)
        return max(dfs(root))
