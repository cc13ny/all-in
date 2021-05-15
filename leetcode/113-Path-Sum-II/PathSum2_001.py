# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root == None:
            return []
        res = []
        stack = []
        stack1 = []
        marked = set()
        stack.append(root)
        stack1.append(root.val)
        s = root.val
        while len(stack) != 0:
            p = stack[len(stack) - 1]

            if p.left == None and p.right == None:
                if s == sum:
                    res.append(stack1)
                s -= stack1[len(stack1) - 1]
                stack1 = stack1[:len(stack1) - 1]
                marked.add(stack.pop())
            elif p.left != None and p.left not in marked:
                s += p.left.val
                stack.append(p.left)
                stack1.append(p.left.val)
            elif p.right != None and p.right not in marked:
                s += p.right.val
                stack.append(p.right)
                stack1.append(p.right.val)
            else:
                p = stack.pop()
                stack1.pop()
                s -= p.val
                marked.add(p)

        return res
