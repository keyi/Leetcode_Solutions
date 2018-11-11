# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        cur = [root]
        while cur:
            val, nex = [], []
            for x in cur:
                if x.left:
                    nex.append(x.left)
                if x.right:
                    nex.append(x.right)
                val.append(x.val)
            cur = nex
            ans.append(val)
        return ans
