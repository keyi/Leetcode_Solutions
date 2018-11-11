/**
 * Definition for binary tree with next temper.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null)
			return;
		TreeLinkNode temp = root.next;
		while (temp != null) {
			if (temp.left != null) {
				temp = temp.left;
				break;
			} else if (temp.right != null) {
				temp = temp.right;
				break;
			} else
				temp = temp.next;
		}
		if (root.right != null) {
			root.right.next = temp;
		}
		if (root.left != null) {
			root.left.next = root.right == null ? temp : root.right;
		}
		connect(root.right);
		connect(root.left);
    }
}