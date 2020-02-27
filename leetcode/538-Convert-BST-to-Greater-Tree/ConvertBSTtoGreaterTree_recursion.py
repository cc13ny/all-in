# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def traverse(node, prev_sum):
            if node:
                prev_sum = traverse(node.right, prev_sum)
                node.val += prev_sum
                prev_sum = traverse(node.left, node.val)
            return prev_sum
        traverse(root, 0)
        return root
