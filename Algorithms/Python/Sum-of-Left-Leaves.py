# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Space O(1), Time O(N)


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0
            l, r = root.left, root.right
            if l and not l.left and not l.right:
                return l.val + helper(r)
            else:
                return helper(l) + helper(r)

        return helper(root)
