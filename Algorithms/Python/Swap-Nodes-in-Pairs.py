# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node and node.next and node.next.next:
            slow = node.next
            fast = node.next.next
            node.next = fast
            slow.next = fast.next
            fast.next = slow
            node = node.next.next
        return dummy.next
