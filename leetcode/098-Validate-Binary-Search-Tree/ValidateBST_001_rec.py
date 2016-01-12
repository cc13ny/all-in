# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
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
