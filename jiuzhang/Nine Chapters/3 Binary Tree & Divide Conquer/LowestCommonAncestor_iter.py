"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        dumpy = TreeNode(0)
        dumpy.left = root
        stack = [dumpy]

        candicate, ancestor, ancestor_id = None, None, 0

        while stack != [] and stack[0] is not None:
            node = stack.pop()
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) == ancestor_id:
                ancestor = stack[-1]
                ancestor_id -= 1
            node = stack.pop()
            if node == A or node == B:
                if candicate is None:
                    candicate = node
                    ancestor = node
                    ancestor_id = len(stack)
                else:
                    return ancestor
        
            stack.append(node.right)
        if candicate:
            return candicate
        return None
