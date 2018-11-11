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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	ListNode head = null;
		ListNode node = null;
		if (l1 == null)
			return l2;
		if (l2 == null)
			return l1;
		while (l1 != null && l2 != null) {
			if (l1.val <= l2.val) {
				if (node == null) {
					node = l1;
					head = l1;
				} else {
					node.next = l1;
					node = node.next;
				}
				l1 = l1.next;
			} else {
				if (node == null) {
					node = l2;
					head = l2;
				} else {
					node.next = l2;
					node = node.next;
				}
				l2 = l2.next;
			}
		}
		if (l1 != null) {
			node.next = l1;
		} else if (l2 != null) {
			node.next = l2;
		}
		return head;
    }
}