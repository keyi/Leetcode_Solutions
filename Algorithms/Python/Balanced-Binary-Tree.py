# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def getDepth(node, depth):
            if not node:
                return depth
            depth += 1
            return max(getDepth(node.left, depth), getDepth(node.right, depth))

        def comparelr(nodeA, nodeB):
            if abs(getDepth(nodeA, 0) - getDepth(nodeB, 0)) > 1:
                return False
            a, b = True, True
            if nodeA:
                a = comparelr(nodeA.left, nodeA.right)
            if nodeB:
                b = comparelr(nodeB.left, nodeB.right)
            return a and b

        if not root:
            return True
        return comparelr(root.left, root.right)
