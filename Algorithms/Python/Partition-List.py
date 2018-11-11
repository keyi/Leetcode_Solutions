# Definition for singly-linked list.
# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast.next and fast.next.val < x:
            slow = fast.next
            fast = fast.next
        if not fast.next:
            return head
        pos = fast.next
        fast = fast.next
        while fast.next:
            if fast.next.val < x:
                temp = fast.next.next
                slow.next = fast.next
                slow = slow.next
                slow.next = pos
                fast.next = temp
            else:
                fast = fast.next
        return dummy.next
