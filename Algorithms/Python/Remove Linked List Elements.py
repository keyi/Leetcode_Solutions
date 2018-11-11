# Definition for singly-linked list.
# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            if fast.val == val:
                fast = fast.next
                slow.next = fast
            else:
                slow, fast = slow.next, fast.next
        return dummy.next
