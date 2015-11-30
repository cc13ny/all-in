/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dumpy = new ListNode(0);
        ListNode p = dumpy;
        int c = 0;
        
        while ((l1 != null) && (l2 != null)) {
            p.next = new ListNode((l1.val + l2.val + c) % 10);
            c = (l1.val + l2.val + c) / 10;
            l1 = l1.next;
            l2 = l2.next;
            p = p.next;
        }
        
        while (l1 != null) {
            p.next = new ListNode((l1.val  + c) % 10);
            c = (l1.val + c) / 10;
            l1 = l1.next;
            p = p.next;
        }
        
        while (l2 != null) {
            p.next = new ListNode((l2.val  + c) % 10);
            c = (l2.val + c) / 10;
            l2 = l2.next;
            p = p.next;
        }
        
        if (c != 0) {
            p.next = new ListNode(c);
        }
        
        return dumpy.next;
    }
}
