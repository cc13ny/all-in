"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        postorder, stack = [], [root]

        while stack != [] and stack[0] is not None:
            node = stack.pop()
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack[-1].right

            if node is None:
                while stack != [] and stack[-1].right == node:
                    node = stack.pop()
                    postorder.append(node.val)

            if stack != []:
                node = stack[-1].right
                stack.append(node)          

        return postorder
