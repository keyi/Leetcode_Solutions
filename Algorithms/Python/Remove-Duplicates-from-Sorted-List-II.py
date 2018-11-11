# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(head.val - 1)
        dummy.next = head
        slow, fast, preval = dummy, dummy.next, dummy.val
        while fast and fast.next:
            if fast.val == fast.next.val:
                preval = fast.val
                fast = fast.next.next
            elif fast.val != fast.next.val:
                if fast.val != preval:
                    slow.next, preval = fast, fast.val
                    slow = slow.next
                else:
                    preval = fast.val
                fast = fast.next
        if (not fast) or (fast and fast.val != preval):
            slow.next = fast
        else:
            slow.next = None
        return dummy.next
