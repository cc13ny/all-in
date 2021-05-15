# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0

        num = 0
        stack = []
        stack.append(root)
        flag = False
        while len(stack) != 0:
            nnext = []
            for t in stack:
                if t != None:
                    if t.left == None and t.right == None:
                        return num + 1
                    nnext.append(t.left)
                    nnext.append(t.right)
            stack = nnext
            num = num + 1
