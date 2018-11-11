# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):

        def getPath(node, pathlist):
            if not node.left and not node.right:
                ans.append(pathlist)
                return
            if node.left:
                getPath(node.left, pathlist + '->' + str(node.left.val))
            if node.right:
                getPath(node.right, pathlist + '->' + str(node.right.val))

        if not root:
            return []
        ans = []
        getPath(root, str(root.val))
        return ans
