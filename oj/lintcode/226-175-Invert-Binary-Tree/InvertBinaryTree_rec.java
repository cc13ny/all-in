/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root != null) { // base case: NULL
            TreeNode l = root.left;
            TreeNode r = root.right;
            
            // swap two subtrees
            root.left = r;
            root.right = l;
            
            // invert two subtrees
            this.invertBinaryTree(l);
            this.invertBinaryTree(r);
        }
    }
}