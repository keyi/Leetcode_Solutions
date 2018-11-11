# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# METHOD 1: Space: O(1), Time: O(n) --- BFS


class Solution(object):

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        head = root
        while head:
            pre, cur, nex = None, head, None
            while cur:
                if not nex:
                    nex = cur.left if cur.left else cur.right
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    pre = cur.right
                cur = cur.next
            head = nex

# METHOD 2: Space: O(logN), Time: O(n) --- DFS


class Solution(object):

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        temp = root.next
        while temp:
            if temp.left:
                temp = temp.left
                break
            if temp.right:
                temp = temp.right
                break
            temp = temp.next
        if root.right:
            root.right.next = temp
        if root.left:
            root.left.next = root.right if root.right else temp
        self.connect(root.right)
        self.connect(root.left)
