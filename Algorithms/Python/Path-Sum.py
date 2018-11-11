# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def getSum(node, val):
            if not node.left and not node.right:
                ans.append(val)
                return
            if node.left:
                getSum(node.left, val + node.left.val)
            if node.right:
                getSum(node.right, val + node.right.val)

        if not root:
            return False
        ans = []
        getSum(root, root.val)
        return sum in ans
