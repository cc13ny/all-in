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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        isbalanced, h = self.isBalancedandHeight(root)
        return isbalanced

    def isBalancedandHeight(self, root):
        if root is None:
            return True, 0

        l, r = root.left, root.right
        l_balanced, l_h = self.isBalancedandHeight(l)
        if not l_balanced:
            return False, 0

        r_balanced, r_h = self.isBalancedandHeight(r)
        if not r_balanced:
            return False, 0

        if abs(l_h - r_h) < 2:
            return True, max(l_h, r_h) + 1

        return False, 0
