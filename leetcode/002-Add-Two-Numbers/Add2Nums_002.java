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
        ListNode dump = new ListNode(0);
        ListNode p = dump;
        int i = 0, c = 0;
        
        while(l1 != null && l2 != null) {
            p.next = new ListNode(0);
            p = p.next;
            p.val = (l1.val + l2.val + c) % 10;
            c = (l1.val + l2.val + c) / 10;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while(l1 != null) {
            p.next = new ListNode(0);
            p = p.next;
            p.val = (l1.val + c) % 10;
            c = (l1.val + c) / 10;
            l1 = l1.next;
        }
        
        while(l2 != null) {
            p.next = new ListNode(0);
            p = p.next;
            p.val = (l2.val + c) % 10;
            c = (l2.val + c) / 10;
            l2 = l2.next;
        }
        
        if(c == 1)
            p.next = new ListNode(1);
        
        return dump.next;
    }
}
