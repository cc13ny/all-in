/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 * int val;
 * TreeLinkNode left, right, next;
 * TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        TreeLinkNode parent = root;
        if (parent != null) {

            TreeLinkNode child = parent.left;
            TreeLinkNode leftmostchild = child;

            while (leftmostchild != null) {
                if (child == parent.left) {
                    child.next = parent.right;
                } else {
                    parent = parent.next;
                    if (parent != null) {
                        child.next = parent.left;
                    }
                }
                child = child.next;

                if (child == null) {
                    parent = leftmostchild;
                    child = parent.left;
                    leftmostchild = child;
                }
            }
        }
    }
}
