/**
 * Definition for ListNode.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int val) {
 * this.val = val;
 * this.next = null;
 * }
 * }
 */
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        // write your code here
        if (head == null) {
            return null;
        }
        ListNode dumpy = new ListNode(0);
        dumpy.next = head;
        ListNode p = head;
        ListNode tmp;

        while (p.next != null) {
            tmp = p.next;
            p.next = tmp.next;
            tmp.next = dumpy.next;
            dumpy.next = tmp;
        }

        return dumpy.next;
    }
}