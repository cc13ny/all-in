# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        stack = []
        res = []
        stack.append(root)
        while len(stack)!= 0:
            tmp = []
            nnext = []
            for i in range(len(stack)):
                if stack[i] != None:
                    tmp.append(stack[i].val)
                    nnext.append(stack[i].left)
                    nnext.append(stack[i].right)
            if len(tmp) != 0:
                res.append(tmp)
            stack = nnext
            
        return res
