/ **
*Definition
for binary tree
    *public


class TreeNode {
* int val;
* TreeNode left;
* TreeNode right;
* TreeNode(int x) {val = x;}
*}

* /
import java.util.Hashtable;

public


class Solution {
public TreeNode buildTree(int[] inorder, int[] postorder) {
int len = inorder.length;
if (len == 0)


return null;

Hashtable < Integer, Integer > postb = new
Hashtable < Integer, Integer > ();
Hashtable < Integer, Integer > intb = new
Hashtable < Integer, Integer > ();

int
root = postorder[len - 1];
TreeNode
tree_root = new
TreeNode(root);

for (int i = 0; i < len; i++){
    postb.put(postorder[i], i);
intb.put(inorder[i], i);
}

for (int j = len - 2; j > -1; j--){
    int num = postorder[j];
int inloc = intb.get(num);
TreeNode next = tree_root;
while (true){
if (inloc < intb.get(next.val)){
if (next.left == null){
next.left = new TreeNode(num);
break;
}
else {
next = next.left;
}
}
else {
if (next.right == null)
{
next.right = new
TreeNode(num);
break;
}
else {
next = next.right;
}
}
}
}

return tree_root;
}
}
