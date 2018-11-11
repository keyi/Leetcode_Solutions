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
    public ListNode swapPairs(ListNode head) {
    	ListNode curr = new ListNode(-1);
		curr.next = head;
		head = curr;
		while (curr.next != null && curr.next.next != null) {
			ListNode temp = curr.next.next.next;
			curr.next.next.next = curr.next;
			curr.next = curr.next.next;
			curr.next.next.next = temp;
			curr = curr.next.next;
		}
		return head.next; 
    }
}