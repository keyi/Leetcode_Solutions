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
    public boolean isSymmetric(TreeNode root) {
		if (root == null)
			return true;
		return isMirror(root.left, root.right);
	}

	public boolean isMirror(TreeNode treeA, TreeNode treeB) {
		if (treeA == null && treeB == null)
			return true;
		if (treeA == null || treeB == null)
			return false;
		if (treeA.val == treeB.val)
			return isMirror(treeA.left, treeB.right)
					&& isMirror(treeA.right, treeB.left);
		return false;
	}
}