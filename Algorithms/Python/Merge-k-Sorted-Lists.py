# Time(NK * log(K))


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def daq(start, end):
            if start >= end:
                return lists[start]
            mid = (start + end) // 2
            left, right = daq(start, mid), daq(mid + 1, end)
            return mergeTwoLists(left, right)

        def mergeTwoLists(list1, list2):
            dummy = ListNode(-1)
            head = dummy
            head1, head2 = list1, list2
            while head1 and head2:
                if head1.val < head2.val:
                    head.next = head1
                    head1 = head1.next
                else:
                    head.next = head2
                    head2 = head2.next
                head = head.next
            head.next = head1 if head1 else head2
            return dummy.next

        if not lists:
            return None
        return daq(0, len(lists) - 1)
