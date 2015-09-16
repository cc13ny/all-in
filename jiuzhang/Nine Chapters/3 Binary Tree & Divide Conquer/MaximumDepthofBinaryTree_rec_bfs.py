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
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        l, r = root.left, root.right
        lDepth, rDepth = self.maxDepth(l), self.maxDepth(r)
        return max(lDepth, rDepth) + 1
