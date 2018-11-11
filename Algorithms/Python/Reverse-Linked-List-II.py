# Definition for singly-linked list.
# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or not head:
            return head
        dummy = ListNode(-1)
        node = head
        left, mid, right = None, None, None
        count = 1
        while node:
            if count < m:
                left = node
                node = node.next
            elif m <= count and count <= n:
                if count == m:
                    mid = node
                temp = node.next
                node.next = dummy.next
                dummy.next = node
                node = temp
            else:
                right = node
                break
            count += 1
        mid.next = right
        if not left:
            return dummy.next
        else:
            left.next = dummy.next
            return head
