# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        
        if root == None: 
            return []
        
        lv = self.rightSideView(root.left)
        rv = self.rightSideView(root.right)
        
        if len(lv) > len(rv): 
            rv[len(rv):] = lv[len(rv):] 

        return [root.val].extend(rv)
