# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        left = head
        right, slow.next = slow.next, None
        dummy = ListNode(-1)
        while right:
            temp = right.next
            right.next = dummy.next
            dummy.next = right
            right = temp
        right = dummy.next
        while left and right:
            ltemp, rtemp = left.next, right.next
            left.next = right
            right.next = ltemp
            left, right = ltemp, rtemp
