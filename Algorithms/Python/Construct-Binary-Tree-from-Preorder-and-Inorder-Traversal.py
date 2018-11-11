# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(preStart, preEnd, inStart, inEnd):
            if not preorder[preStart:preEnd] or not inorder[inStart:inEnd]:
                return None
            value = preorder[preStart:preEnd][0]
            pos = inorder[inStart:inEnd].index(value)
            node = TreeNode(value)
            node.left = dfs(preStart + 1, preStart + 1 +
                            pos, inStart, inStart + pos)
            node.right = dfs(preStart + 1 + pos, preEnd,
                             inStart + pos + 1, inEnd)
            return node

        l1, l2 = len(preorder), len(inorder)
        return dfs(0, l1, 0, l2)


# METHOD 2  (MLE)
# class Solution(object):

#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         def dfs(preorder, inorder):
#             if not preorder or not inorder:
#                 return None
#             pos = inorder.index(preorder[0])
#             node = TreeNode(inorder[pos])
#             node.left = dfs(preorder[1:pos + 1], inorder[:pos])
#             node.right = dfs(preorder[pos + 1:], inorder[pos + 1:])
#             return node

#         return dfs(preorder, inorder)
