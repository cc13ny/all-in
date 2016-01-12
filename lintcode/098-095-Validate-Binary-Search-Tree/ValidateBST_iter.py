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
        stack, pre = [root], None
        while stack != [] and stack[0] is not None:
            node = stack.pop()
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre is not None and pre.val >= node.val:
                return False
            pre = node
            stack.append(node.right)
        return True
