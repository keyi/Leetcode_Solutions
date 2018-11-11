# Definition for singly-linked list.
# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        l = dummy
        while l1 and l2:
            if(l1.val <= l2.val):
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
        return dummy.next
