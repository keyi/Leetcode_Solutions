# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# METHOD 1  Recrusion
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def rev(node):
            if not node:
                return [None, None]
            [start, end] = rev(node.next)
            if end:
                end.next = node
                node.next = None
                return [start, node]
            else:
                return [node, node]

        return rev(head)[0]

# METHOD 3  Iteration


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
            # dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
