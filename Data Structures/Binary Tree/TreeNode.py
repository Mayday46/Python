
class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


# node1 = TreeNode(1)
# node2 = TreeNode(3)
# node3 = TreeNode(1)
# node4 = TreeNode(6)

# node1.left = node2
# node2.left = node3
# node3.left = node4

def check_tree(root):
    # Time Complexity -> O(1)
    return root.left.val + root.right.val == root.val

# print(check_tree(node1))

def left_most(root):

    if root is None:
        return None
    
    while root.left is not None:
        root = root.left
    return root.val
    # currNode = root
    # while currNode.left:
    #     currNode = currNode.left
    # return currNode.val

# print(left_most(node1))

'''
            1
           /
          3
         /
        1
       /
      6
'''



# def inorder_traversal(root):
#     res = []

#     def traverse(root):
#         if not root:
#             return
#         traverse(root.left)
#         res.append(root.val)
#         traverse(root.right)
#     traverse(root)
#     return res

def inorder_traversal(root):
    if not root: # If the root is empty
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# node1 = TreeNode(10)
# node2 = TreeNode(3)
# node3 = TreeNode(2)
# node4 = TreeNode(4)

# node5 = TreeNode(16)
# node6 = TreeNode(15)
# node7 = TreeNode(23)



# node1.left = node2
# node1.right = node5

# node2.left = node3
# node2.right = node4

# node5.left = node6
# node5.right = node7


# print(inorder_traversal(node1))

def size(root, nodes = []):
    if root is not None:
        size(root = root.left, nodes = nodes)
        nodes.append(root.val)
        size(root = root.right, nodes = nodes)
    return len(nodes)

# print(size(node1))

def find(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value)

# print(find(node1, 10))

def descending_leaves(root):
    def helper(root, res):
        if root is None:
            return
        if root.left is None and root.right is None:
            # Check if this node has a left or right child
            res.append(root.val)
        helper(root.left, res)
        helper(root.right, res)
    result = []
    helper(root = root, result = result)
    return result


def add(root, data):

    if not root: # If the tree is empty, meaning no root
        # newNode = TreeNode(data)
        # root = newNode
        return TreeNode(data)
    # Else root is not None
    
    if data > root.val: # If the data is larger than current root, go to the right
        if root.right is None:
            newNode = TreeNode(data)
            root.right = newNode
        else:
            add(root.right, data)
    else:
        # If the data is less than current root.val, go to the left
        if root.left is None:
            newNode = TreeNode(data)
            root.left = newNode
        else:
            add(root.left, data)
    return root

node1 = add(None, 10)
node2 = add(root = node1, data = 5)
node3 = add(root = node1, data = 20)
node4 = add(root = node1, data = 64)
node5 = add(root = node1, data = 24)
print(inorder_traversal(node1))
# print(node1.val)
# print(node1.left.val)
# print(node1.right.val)

