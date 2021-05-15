class Solution:
    # @param root, a tree node
    # @return a list of integers
    def iterative_inorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                list.append(root.val)
                root = root.right
        return list

    def recursive_inorder(self, root, list):
        if root:
            self.inorder(root.left, list)
            list.append(root.val)
            self.inorder(root.right, list)

    def inorderTraversal(self, root):
        list = []
        self.iterative_inorder(root, list)
        return list
