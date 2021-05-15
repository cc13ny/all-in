class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def valOrder(root):
    val, h = 0, 0
    stack = [(root, val, h)]
    arr, minarr = [], []
    start = 0
    while stack != [] and stack[0][0] is not None:
        node, val, h = stack.pop()
        while node is not None:
            stack.append((node, val, h))

            ###############################
            idx = val - start
            if idx < 0:
                start = val
                idx = 0
                arr.insert(0, [])
                minarr.insert(0, h)
            if idx >= len(arr):
                arr.append([])
                minarr.append(h)
            idx_in_h = h - minarr[idx]
            if idx_in_h < 0:
                minarr[idx] = h
                arr[idx].insert(0, [node.val])
            elif idx_in_h >= len(arr[idx]):
                arr[idx].append([node.val])
            else:
                arr[idx][idx_in_h].append(node.val)
            ###############################

            val -= 1
            h += 1
            node = node.left
        node, val, h = stack.pop()
        stack.append((node.right, val + 1, h + 1))

    for ls in arr:
        for group in ls:
            for e in group:
                print
                e


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

h = TreeNode(8)

a.left = b
a.right = c
c.left = d
d.left = e
d.right = g
e.left = f
f.left = h
h.left = TreeNode(9)
g.left = TreeNode(10)

valOrder(a)
