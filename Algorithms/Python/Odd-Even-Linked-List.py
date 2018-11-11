# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head


# METHOD 2


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        odd, even = ListNode(-1), ListNode(-1)
        otemp, etemp = odd, even
        oddStatus = True
        while head:
            if oddStatus:
                otemp.next = head
                otemp = otemp.next
                oddStatus = False
            else:
                etemp.next = head
                etemp = etemp.next
                oddStatus = True
            head = head.next
        etemp.next = None
        otemp.next = even.next
        return odd.next
