# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(cur):
            if cur:
                mid = len(cur) // 2
                node = TreeNode(cur[mid])
                node.left = dfs(cur[:mid])
                node.right = dfs(cur[mid + 1:])
                return node
            else:
                return None

        return dfs(nums)

# METHOD 2


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(start, end):
            if start < end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = dfs(start, mid)
                node.right = dfs(mid + 1, end)
                return node
            else:
                return None

        return dfs(0, len(nums))
