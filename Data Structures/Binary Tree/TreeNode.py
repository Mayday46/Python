
class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


def check_tree(root):
    # Time Complexity -> O(1)
    return root.left.val + root.right.val == root.val


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


'''
            1
           /
          3
         /
        1
       /
      6
'''
def right_most(root):
    if not root:
        return None
    
    while root.right is not None:
        root = root.right
    return root.val


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

def preorder_traversal(root, result = []):
    '''
    At first visit the root then traverse left subtree and then traverse the right subtree.
    '''
    if not root:
        return []
    result.append(root.val)
    preorder_traversal(root= root.left, result = result)
    preorder_traversal(root.right, result)
    return result

def postorder_traversal(root, res = []):
    '''
    At first traverse left subtree then traverse the right subtree and then visit the root.
    '''
    if not root:
        return []
    postorder_traversal(root.left, res)
    postorder_traversal(root.right, res)
    res.append(root.val)
    return res


def size(root, nodes = []):
    if root is not None:
        size(root = root.left, nodes = nodes)
        nodes.append(root.val)
        size(root = root.right, nodes = nodes)
    return len(nodes)


def find(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value)


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


def height(root):
    count = 0
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return max(leftHeight, rightHeight) + 1

def insert(root, data):

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
            insert(root.right, data)
    else:
        # If the data is less than current root.val, go to the left
        if root.left is None:
            newNode = TreeNode(data)
            root.left = newNode
        else:
            insert(root.left, data)
    return root



def remove_bst(root, target):
    if not root:  # If the tree is empty
        return root
    
    if target > root.val:  # Searching in the right subtree
        root.right = remove_bst(root.right, target)
    elif target < root.val:  # Searching in the left subtree
        root.left = remove_bst(root.left, target)
    else:  # We found the node to delete

        # Case 1: Node with no children (leaf node)
        if not root.left and not root.right:
            return None
        
        # Case 2: Node with only one child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Case 3: Node with two children
        # Find the in-order successor (smallest value in the right subtree)
        nodePointer = root.right
        while nodePointer.left:
            nodePointer = nodePointer.left
        root.val = nodePointer.val
        root.right = remove_bst(root.right, nodePointer.val)
    
    return root



def is_univalued(root):
    '''
    A binary Tree is uni-valued if every node in the tree has the same value.
    Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

    '''
    childs = inorder_traversal(root)
    
    for first in range(len(childs)):
        for second in range(first + 1, len(childs)):
            if childs[first] != childs[second]:
                return False
    return True


root = TreeNode(100)
node1 = TreeNode(20)
node2 = TreeNode(10)
node3 = TreeNode(30)
node4 = TreeNode(200)
node5 = TreeNode(150)
node6 = TreeNode(300)

root.left = node1
root.right = node4

node1.left = node2
node1.right = node3

node4.left = node5
node4.right = node6

print(f"Preorder Traversal -> {preorder_traversal(root)}")
print(f"Inorder Traversal -> {inorder_traversal(root)}")
print(f"Postorder Traversal -> {postorder_traversal(root)}")

# insert(node1, 3)
# insert(node1, 6)
# insert(node1, 2)
# insert(node1, 4)
# insert(node1, 7)

# print(inorder_traversal(node1))
# remove_bst(root = node1, target = 4)
# remove_bst(root = node1, target = node1.val)
# print(inorder_traversal(node1))


# print(is_univalued(node1))
