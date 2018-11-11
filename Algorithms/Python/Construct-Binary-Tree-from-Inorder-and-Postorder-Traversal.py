# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def dfs(inStart, inEnd, postStart, postEnd):
            if not inorder[inStart:inEnd] or not postorder[postStart:postEnd]:
                return None
            value = postorder[postStart:postEnd][-1]
            pos = inorder[inStart:inEnd].index(value)
            node = TreeNode(value)
            node.left = dfs(inStart, inStart + pos, postStart, postStart + pos)
            node.right = dfs(inStart + pos + 1, inEnd,
                             postStart + pos, postEnd - 1)
            return node
        l1, l2 = len(inorder), len(postorder)
        return dfs(0, l1, 0, l2)
