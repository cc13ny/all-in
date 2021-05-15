/**
 * Definition for binary tree
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

import java.util.Hashtable;

public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int len = preorder.length;

        if (len == 0) return null;

        Hashtable<Integer, Integer> pretb = new Hashtable<Integer, Integer>();
        Hashtable<Integer, Integer> intb = new Hashtable<Integer, Integer>();

        int root = preorder[0];
        TreeNode tree_root = new TreeNode(root);

        for (int i = 0; i < len; i++) {
            pretb.put(preorder[i], i);
            intb.put(inorder[i], i);
        }


        for (int j = 1; j < len; j++) {
            int num = preorder[j];
            int inloc = intb.get(num);
            TreeNode next = tree_root;
            boolean flag = false;
            while (true) {
                if (inloc < intb.get(next.val)) {
                    if (next.left == null) {
                        next.left = new TreeNode(num);
                        flag = true;
                    } else {
                        next = next.left;
                    }
                } else {
                    if (next.right == null) {
                        next.right = new TreeNode(num);
                        flag = true;
                    } else {
                        next = next.right;
                    }

                }

                if (flag) break;
            }
        }

        return tree_root;
    }
}
