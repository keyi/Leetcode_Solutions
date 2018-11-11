# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, val):
            if not node.left and not node.right:
                ans.append(val)
                return
            if node.left:
                dfs(node.left, node.left.val)
            ans.append(val)
            if node.right:
                dfs(node.right, node.right.val)

        if not root:
            return True
        ans = []
        dfs(root, root.val)
        if len(ans) == 1:
            return True
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True


# METHOD 2
class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, minNum, maxNum):
            if not node:
                return True
            return minNum < node.val and node.val < maxNum and dfs(node.left, minNum, node.val) and dfs(node.right, node.val, maxNum)

        if not root:
            return True
        return dfs(root, -2147483649, 2147483648)
