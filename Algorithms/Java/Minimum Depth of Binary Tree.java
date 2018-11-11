/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int minDepth(TreeNode root) {
		if (root == null)
			return 0;
		return find(root, 1);
	}

	public int find(TreeNode tree, int n) {
		if (tree.left != null && tree.right != null)
			return Math.min(find(tree.left, n + 1), find(tree.right, n + 1));
		else if (tree.left != null)
			return find(tree.left, n + 1);
		else if (tree.right != null)
			return find(tree.right, n + 1);
		else
			return n;
	}

}