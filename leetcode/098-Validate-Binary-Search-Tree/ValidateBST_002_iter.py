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
        stack = [root]
        pre = None

        while stack != [] and stack[0]:
            p = stack.pop()
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre and pre.val >= p.val:
                return False
            pre = p
            stack.append(p.right)

        return True
