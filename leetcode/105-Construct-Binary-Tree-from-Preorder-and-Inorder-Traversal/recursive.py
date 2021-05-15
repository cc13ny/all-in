# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder: root [left sub-tree] [right sub-tree]
        # inorder:  [left sub-tree] root [right sub-tree]
        if len(preorder) != len(inorder) or preorder is None or inorder is None or preorder == [] or inorder == []:
            return None
        root = preorder[0]

        i = 0
        while i < len(inorder):
            if inorder[i] == root:
                break
            i += 1

        root_node = TreeNode(root)
        root_node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root_node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

        return root_node
