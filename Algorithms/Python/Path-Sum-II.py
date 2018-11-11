# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, cur):
            if not node.left and not node.right:
                temp = reduce(lambda x, y: x + y, cur)
                if temp == sum:
                    ans.append(cur)
                return
            if node.left:
                dfs(node.left, cur + [node.left.val])
            if node.right:
                dfs(node.right, cur + [node.right.val])

        if not root:
            return []
        ans = []
        dfs(root, [root.val])
        return ans
