# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
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
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return dfs(0, len(nums))
