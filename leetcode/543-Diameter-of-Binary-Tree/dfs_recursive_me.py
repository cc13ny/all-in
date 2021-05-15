# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, res = self.max_depth(root)
        return res

    def max_depth(self, node: TreeNode) -> int:
        if node is None:
            return -1, 0
        left_depth, left_max = self.max_depth(node.left)
        right_depth, right_max = self.max_depth(node.right)

        return max(left_depth, right_depth) + 1, max(left_depth + right_depth + 2, left_max, right_max)
