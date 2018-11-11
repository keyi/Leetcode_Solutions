# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        numA, numB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            numA += 1
            nodeA = nodeA.next
        while nodeB:
            numB += 1
            nodeB = nodeB.next
        nodeA, nodeB = headA, headB
        if numA > numB:
            for i in range(numA - numB):
                nodeA = nodeA.next
        else:
            for i in range(numB - numA):
                nodeB = nodeB.next
        while nodeA != nodeB:
            nodeA, nodeB = nodeA.next, nodeB.next
        return nodeA
