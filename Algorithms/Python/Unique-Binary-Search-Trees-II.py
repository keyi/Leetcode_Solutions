# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def buildTree(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            s = []
            for i in range(start, end + 1):
                for l in buildTree(start, i - 1):
                    for r in buildTree(i + 1, end):
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        s.append(root)
            return s
        if n == 0:
            return []
        return buildTree(1, n)
