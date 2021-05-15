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
     * @param node: the node in the list should be deleted
     * @return: nothing
     */
    public void deleteNode(ListNode node) {
        /*
         * Replace the val of current node with the val of next node
         * Connect the current node with the next next node of the current node
         */
        node.val = node.next.val;
        node.next = node.next.next;
    }
}