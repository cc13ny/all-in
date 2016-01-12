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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        isVal, mi, ma = self.isValid(root)
        return isVal
    
    def isValid(self, root):
        if not root:
            return True, 0, 0

        l, r = root.left, root.right
        val = root.val
        
        if l:
            isLValid, lmin, lmax = self.isValid(l)
        else:
            isLValid, lmin, lmax = True, val - 1, val - 1
        
        if not isLValid:
            return False, 0, 0
        
        if r:
            isRValid, rmin, rmax = self.isValid(r)
        else:
            isRValid, rmin, rmax = True, val + 1, val + 1
        
        if not isRValid:
            return False, 0, 0
        
        if lmax > val or rmin < val:
            return False, 0, 0
            
        return True, lmin, rmax
