# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(node):
            num = 0
            while node:
                num += 1
                node = node.left
            return num

        def splitTree(node):
            if not node:
                return 0
            hl, hr = getHeight(node.left), getHeight(node.right)
            if hl > hr:
                return 2**hr + splitTree(node.left)
            else:
                return 2**hr + splitTree(node.right)

        return splitTree(root)
