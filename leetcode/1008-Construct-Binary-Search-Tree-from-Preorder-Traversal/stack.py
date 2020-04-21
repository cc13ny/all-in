# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder.pop(0))
        stack = [root]  # store ascendants
        for node_val in preorder:
            if stack and stack[-1].val > node_val:
                stack[-1].left = TreeNode(node_val)
                stack.append(stack[-1].left)
            else:
                curr = None
                while stack and stack[-1].val < node_val:
                    curr = stack.pop()
                stack.append(TreeNode(node_val))
                if curr:
                    curr.right = stack[-1]

        return root