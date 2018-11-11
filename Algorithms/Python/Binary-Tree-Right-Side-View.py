# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# METHOD 1: DFS


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, depth):
            if not node:
                return
            else:
                if depth == len(ans):
                    ans.append([node.val])
                else:
                    ans[depth] += [node.val]
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        if not root:
            return []
        ans = []
        dfs(root, 0)
        return [x[-1] for x in ans]


# METHOD 2: BFS
class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        s = [root]
        ans = []
        while s:
            temp, cur = None, []
            for node in s:
                temp = node.val
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            ans.append(temp)
            s = cur
        return ans
