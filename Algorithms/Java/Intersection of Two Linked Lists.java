/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    	ListNode nodeA = headA;
		ListNode nodeB = headB;
		int lenA = 0, lenB = 0;
		while (nodeA != null) {
			nodeA = nodeA.next;
			lenA++;
		}
		while (nodeB != null) {
			nodeB = nodeB.next;
			lenB++;
		}
		nodeA = headA;
		nodeB = headB;
		if (lenA > lenB) {
			for (int i = 0; i < lenA - lenB; i++)
				nodeA = nodeA.next;
		} else if (lenA < lenB) {
			for (int i = 0; i < lenB - lenA; i++)
				nodeB = nodeB.next;
		}
		while (nodeA != nodeB) {
			nodeA = nodeA.next;
			nodeB = nodeB.next;
		}
		return nodeA;
    }
}