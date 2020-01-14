class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorderPreorderTraversal(root):
    inorder, preorder, stack = [], [], [root]
    while stack != [] and stack[0] is not None:
        node = stack.pop()
        while node is not None:
            
            preorder.append(node.val)
            
            stack.append(node)
            node = node.left
        node = stack.pop()
        
        inorder.append(node.val)
        
        stack.append(node.right)
    return inorder, preorder