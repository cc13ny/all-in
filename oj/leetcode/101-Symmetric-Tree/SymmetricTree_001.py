# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSym(self, l, r):
        if l == None and r != None:
            return False
        if l != None and r == None:
            return False
        if l == None and r == None:
            return True
        if l.val != r.val:
            return False
        return self.isSym(l.left, r.right) & self.isSym(l.right, r.left)
        
    def isSymmetric(self, root):
        if root == None:
            return True
            
        return self.isSym(root.left, root.right)
