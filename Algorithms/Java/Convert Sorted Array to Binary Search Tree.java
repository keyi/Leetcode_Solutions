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
    public TreeNode sortedArrayToBST(int[] num) {
		// if (num.length == 0)
		// 	return null;
		return buildTree(num, 0, num.length - 1);
	}

	public TreeNode buildTree(int[] num, int a, int b) {
		if (a > b)
			return null;
		int mid = (a + b) / 2;
		TreeNode node = new TreeNode(num[mid]);
		node.left = buildTree(num, a, mid - 1);
		node.right = buildTree(num, mid + 1, b);
		return node;
	}
}