"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None or root == A or root == B:
            return root

        l = self.lowestCommonAncestor(root.left, A, B)
        r = self.lowestCommonAncestor(root.right, A, B)

        if l is not None and r is not None:
            return root
        if l is None:
            return r
        if r is None:
            return l
