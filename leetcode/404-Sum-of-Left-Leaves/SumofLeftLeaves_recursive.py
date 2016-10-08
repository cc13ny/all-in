# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, False)
    
    def dfs(self, node, isleft):
        if not node:
            return 0
        if isleft and (not node.left) and (not node.right):
            return node.val
        return self.dfs(node.left, True) + self.dfs(node.right, False)
