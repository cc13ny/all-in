# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False

        diff = sum - root.val

        if root.left == None and root.right == None and diff == 0:
            return True
        a = self.hasPathSum(root.left, diff)
        b = self.hasPathSum(root.right, diff)

        return a or b
