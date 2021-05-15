/**
 * Definition for binary tree
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

import java.util.Stack;

public class BSTIterator {
    private Stack<TreeNode> stack;
    private TreeNode curt;

    public BSTIterator(TreeNode root) {
        stack = new Stack<TreeNode>();
        curt = root;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return (curt != null) || (!stack.empty());
    }

    /** @return the next smallest number */
    public int next() {
        while (curt != null) {
            stack.push(curt);
            curt = curt.left;
        }
        TreeNode res = stack.pop();
        curt = res.right;

        return res.val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
