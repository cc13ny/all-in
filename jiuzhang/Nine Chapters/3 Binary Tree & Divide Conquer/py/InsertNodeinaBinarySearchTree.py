"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        pt = root
        while pt:
            if pt.val < node.val:
                if pt.right is None:
                    pt.right = node
                    pt = None
                else:
                    pt = pt.right
            else:
                if pt.left is None:
                    pt.left = node
                    pt = None
                else:
                    pt = pt.left
        return root
