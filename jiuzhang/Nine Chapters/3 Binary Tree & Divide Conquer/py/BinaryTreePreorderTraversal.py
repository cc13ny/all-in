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
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        arrlist, stack = [], [root]

        while stack != [] and stack[0] is not None:
            node = stack.pop()
            while node is not None:
                arrlist.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            stack.append(node.right)

        return arrlist
