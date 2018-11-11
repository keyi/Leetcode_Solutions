# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
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
        node, flag = dummy, 0
        while l1 or l2:
            temp = flag
            if l1:
                temp, l1 = temp + l1.val, l1.next
            if l2:
                temp, l2 = temp + l2.val, l2.next
            temp, flag = temp % 10, temp // 10
            node.next = ListNode(temp)
            node = node.next
        if flag:
            node.next = ListNode(flag)
        return dummy.next
