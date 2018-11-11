# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        dummy = ListNode(-1)
        slow, fast, mid = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            mid = slow.next
            slow.next, dummy.next, slow = dummy.next, slow, slow.next
        left = dummy.next
        right = mid if not fast else mid.next
        while left and right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
