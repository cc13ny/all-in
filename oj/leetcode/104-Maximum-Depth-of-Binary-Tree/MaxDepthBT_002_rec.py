# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        lMaxDepth = self.maxDepth(root.left)
        rMaxDepth = self.maxDepth(root.right)
        return max(lMaxDepth, rMaxDepth) + 1
