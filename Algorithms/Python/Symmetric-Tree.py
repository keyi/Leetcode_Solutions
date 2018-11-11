# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def comparelr(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            elif nodeA and nodeB:
                return (nodeA.val == nodeB.val) and comparelr(nodeA.left, nodeB.right) and comparelr(nodeA.right, nodeB.left)
            else:
                return False
        if not root:
            return True
        return comparelr(root.left, root.right)
