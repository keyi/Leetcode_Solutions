# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):

#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        dummy = RandomListNode(-1)
        prev, cur, dic = dummy, head, {}
        while cur:
            temp = RandomListNode(cur.label)
            dic[cur] = temp
            prev.next = temp
            prev, cur = prev.next, cur.next

        cur = head
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dummy.next
