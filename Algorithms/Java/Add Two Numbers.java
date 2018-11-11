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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      ListNode sum = new ListNode(0);
		ListNode s = sum;
		int carry = 0;
		while (l1 != null || l2 != null || carry != 0) {
			if (l1 != null) {
				s.val += l1.val;
				l1 = l1.next;
			}
			if (l2 != null) {
				s.val += l2.val;
				l2 = l2.next;
			}
			s.val += carry;
			carry = s.val / 10;
			s.val %= 10;
			if (l1 != null || l2 != null || carry != 0) {
				s.next = new ListNode(0);
				s = s.next;
			}
		}
		return sum;
    }
}

					// ATNOTHET METHOD // 
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
// public class Solution {
//     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//         String num1 = "", num2 = "";
// 		while (l1 != null) {
// 			num1 += l1.val;
// 			l1 = l1.next;
// 		}
// 		long n1 = 0;
// 		for (int i = 0; i < num1.length(); i++)
// 			n1 += (num1.charAt(i) - '0') * Math.pow(10, i);
// 		while (l2 != null) {
// 			num2 += l2.val;
// 			l2 = l2.next;
// 		}
// 		long n2 = 0;
// 		for (int i = 0; i < num2.length(); i++)
// 			n2 += (num2.charAt(i) - '0') * Math.pow(10, i);
// 		long n = n1 + n2;
// 		String s = String.valueOf(n);
// 		int k = s.length();
// 		ListNode head = new ListNode(0);
// 		ListNode res = head;
// 		for (int i = 0; i < k; i++) {
// 			head.val = (int) (n % 10);
// 			n = (n - head.val) / 10;
// 			if (i == k - 1) {
// 				break;
// 			}
// 			head.next = new ListNode(0);
// 			head = head.next;
// 		}
// 		return res;
//     }
// }