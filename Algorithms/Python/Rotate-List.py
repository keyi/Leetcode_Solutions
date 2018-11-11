# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        k %= l
        if k == 0:
            return head
        dummy = ListNode(-1)
        node = head
        count = 0
        while node:
            count += 1
            if count == l - k:
                dummy.next = node.next
                node.next = None
                break
            node = node.next
        node = dummy.next
        while node.next:
            node = node.next
        node.next = head
        return dummy.next
