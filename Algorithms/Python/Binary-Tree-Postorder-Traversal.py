# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# METHOD 1: DFS


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            traversal(node.right)
            ans.append(node.val)

        ans = []
        traversal(root)
        return ans


# METHOD 2: Stack

class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, stack = [], [root]
        pre = None
        while stack:
            cur = stack[-1]
            if (not cur.left and not cur.right) or (pre and (pre == cur.left or pre == cur.right)):
                ans.append(cur.val)
                pre = cur
                stack.pop()
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return ans
