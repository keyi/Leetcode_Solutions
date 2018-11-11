# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node, depth):
            depth += 1
            if not node.left and not node.right:
                return depth
            elif node.left and not node.right:
                return getDepth(node.left, depth)
            elif not node.left and node.right:
                return getDepth(node.right, depth)
            else:
                return min(getDepth(node.left, depth), getDepth(node.right, depth))
        if not root:
            return 0
        return getDepth(root, 0)
