# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node, depth):
            if not node:
                return depth
            return max(getDepth(node.left, depth + 1), getDepth(node.right, depth + 1))
        return getDepth(root, 0)
