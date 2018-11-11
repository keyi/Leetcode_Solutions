class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class bstMaintain(object):

    def __init__(self):
        self.root = None

    def addNode(self, x):
        node = self.root
        prev = None
        while node:
            if node.val == x:
                return
            elif node.val < x:
                prev = node
                node = node.right
            else:
                prev = node
                node = node.left
        cur = TreeNode(x)
        if not prev:
            self.root = cur
        elif prev.val < x:
            prev.right = cur
        else:
            prev.left = cur
        return

    def iscontainNode(self, x):
        node = self.root
        while node:
            if node.val == x:
                return True
            elif node.val < x:
                node = node.right
            else:
                node = node.left
        return False

    def deleteNode(self, x):
        if not self.iscontainNode(x):
            return False
        prev = None
        node = self.root
        while node:
            if node.val == x:
                break
            elif node.val < x:
                prev = node
                node = node.right
            else:
                prev = node
                node = node.left

        if not node.left and not node.right:  # the leaf node
            if not prev:  # root node
                self.root = None
            elif prev.left == node:
                prev.left = None
            else:
                prev.right = None
        elif not node.left and node.right:  # only has right child
            if not prev:  # root node
                self.root = node.right
            elif prev.left == node:
                prev.left = node.right
            else:
                prev.right = node.right
        elif node.left and not node.right:  # only has left child
            if not prev:  # root node
                self.root = node.left
            elif prev.left == node:
                prev.left = node.left
            else:
                prev.right = node.left
        else:  # has both left and right child
            prev = node
            leftNode = node.left
            while leftNode.right:
                prev = leftNode
                leftNode = leftNode.right
            node.val, leftNode.val = leftNode.val, node.val
            if prev.left == node:
                prev.left = None
            else:
                prev.right = None


BST = bstMaintain()
for i in range(10):
    BST.addNode(i)
print(BST.iscontainNode(1))
print(BST.iscontainNode(11))
print(BST.deleteNode(5))
print(BST.deleteNode(5))
print(BST.iscontainNode(5))
