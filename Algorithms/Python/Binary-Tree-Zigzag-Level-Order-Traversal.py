# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        s, level = [root], 1
        while s:
            cur, nums = [], []
            for x in s:
                nums.append(x.val)
                if x.left:
                    cur.append(x.left)
                if x.right:
                    cur.append(x.right)
            ans += [nums] if level % 2 else [nums[::-1]]
            s, level = cur, level + 1
        return ans
