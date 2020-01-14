/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<String>();
        if (root == null) {
            return res;
        }
        
        List<String> res1 = binaryTreePaths(root.left);
        List<String> res2 = binaryTreePaths(root.right);
        String head = Integer.toString(root.val);
        for(String str : res1) {
            res.add(head + "->" + str);
        }
        
        for(String str : res2) {
            res.add(head + "->" + str);
        }
        
        if (res1.size() == 0 && res2.size() == 0) {
            res.add(head);
        }
        
        return res;
    }
}
