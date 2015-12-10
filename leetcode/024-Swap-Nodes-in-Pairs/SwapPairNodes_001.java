/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dumpy = new ListNode(0);
        dumpy.next = head;
        
        ListNode p = dumpy;
        
        while (p.next != null && p.next.next != null) {
            ListNode tmp = p.next;
            p.next = tmp.next;
            tmp.next = p.next.next;
            p.next.next = tmp;
            p = tmp;
        }
        
        return dumpy.next;
    }
}
