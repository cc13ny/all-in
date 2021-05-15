# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        totMax, branchMax = self.maxBranchandPathSum(root)
        return totMax

    def maxBranchandPathSum(self, root):
        if root is None:
            return 0, 0
        l, r = root.left, root.right
        if l is None and r is None:
            return root.val, root.val

        lTotMax, lBranchMax = self.maxBranchandPathSum(root.left)
        rTotMax, rBranchMax = self.maxBranchandPathSum(root.right)

        lRootBranchMax = root.val + max(lBranchMax, 0)
        rRootBranchMax = root.val + max(rBranchMax, 0)

        if l is None:
            rootTotMax = max(rTotMax, rRootBranchMax)
            return rootTotMax, rRootBranchMax

        if r is None:
            rootTotMax = max(lTotMax, lRootBranchMax)
            return rootTotMax, lRootBranchMax

        rootTreeMax = root.val + max(lBranchMax, 0) + max(rBranchMax, 0)
        rootTotMax = max(lTotMax, rTotMax, rootTreeMax)

        rootBranchMax = max(lRootBranchMax, rRootBranchMax)

        return rootTotMax, rootBranchMax
