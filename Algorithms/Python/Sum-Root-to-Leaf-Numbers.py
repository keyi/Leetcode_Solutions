# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, val):
            if not node.left and not node.right:
                ans.append(val)
            if node.left:
                dfs(node.left, 10 * val + node.left.val)
            if node.right:
                dfs(node.right, 10 * val + node.right.val)

        if not root:
            return 0
        ans = []
        dfs(root, root.val)
        return sum(ans)
