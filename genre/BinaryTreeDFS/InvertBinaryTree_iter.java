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
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        
        TreeNode node, tmp;
        
        while (!stack.isEmpty() && stack.get(0) != null) {
            node = stack.pop();
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            
            stack.push(node.right);
            tmp = node.left;
            node.left = node.right;
            node.right = tmp;
        }
    }
}