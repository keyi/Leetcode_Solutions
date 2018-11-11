# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def doit(root):
            if root:
                values.append(str(root.val))
                doit(root.left)
                doit(root.right)
            else:
                values.append('#')
        values = []
        doit(root)
        return ' '.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = values.pop(0)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = doit()
            root.right = doit()
            return root

        values = data.split(' ')
        return doit()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
