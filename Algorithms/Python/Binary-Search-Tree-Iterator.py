# Space O(h), Time O(1)

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root or self.stack

    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        value = self.root.val
        self.root = self.root.right
        return value


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
