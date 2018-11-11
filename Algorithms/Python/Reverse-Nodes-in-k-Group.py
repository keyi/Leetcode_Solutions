# Definition for singly-linked list.
# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        l, cnt, node = 0, 0, head
        while node:
            node, l = node.next, l + 1
        num = l // k
        if num == 0 or k == 1:
            return head
        rev, dummy = ListNode(-1), ListNode(-1)
        lastEnd, node = dummy, head
        while node and num:
            if cnt < k:
                if cnt == 0:
                    curStart = node
                elif cnt == k - 1:
                    lastEnd.next = node
                    lastEnd = curStart
                node.next, rev.next, node = rev.next, node, node.next
                cnt += 1
            else:
                cnt, num, rev = 0, num - 1, ListNode(-1)
        lastEnd.next = node
        return dummy.next
