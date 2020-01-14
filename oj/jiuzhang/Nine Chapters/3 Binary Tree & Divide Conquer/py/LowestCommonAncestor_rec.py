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
        if not root or root == A or root == B:
            return root

        l = self.lowestCommonAncestor(root.left, A, B)
        r = self.lowestCommonAncestor(root.right, A, B)

        if l and r:
            return root
        if not l:
            return r
        if not r:
            return l
