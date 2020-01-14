# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        
        stack = []
        stack.append(root)
        num = 0
        
        while len(stack) != 0:
            nnext = []
            for t in stack:
                if t != None:
                    nnext.append(t.left)
                    nnext.append(t.right)
            if len(nnext) != 0:
                num = num + 1
            stack = nnext
        return num
