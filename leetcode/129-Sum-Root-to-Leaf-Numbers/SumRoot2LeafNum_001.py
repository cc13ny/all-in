# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if root == None:
            return 0
        stack = []
        marked = set()

        stack.append(root)
        s = str(root.val)
        res = 0

        while len(stack) != 0:
            p = stack[len(stack) - 1]

            if p.left == None and p.right == None:
                res += int(s)
                s = s[:len(s) - 1]
                marked.add(stack.pop())
            elif p.left != None and p.left not in marked:
                p = p.left
                s += str(p.val)
                stack.append(p)
            elif p.right != None and p.right not in marked:
                p = p.right
                s += str(p.val)
                stack.append(p)
            else:
                p = stack.pop()
                s = s[:len(s) - 1]
                marked.add(p)

        return res
