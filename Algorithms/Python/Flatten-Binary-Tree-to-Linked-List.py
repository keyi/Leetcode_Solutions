# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            node = root
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left:
                L, R = node.left, node.right
                node.left = None
                node.right = L
                while node.right:
                    node = node.right
                node.right = R

        dfs(root)
