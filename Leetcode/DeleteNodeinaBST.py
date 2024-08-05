from typing import Optional
'''

450. Delete Node in BST

Given a root node reference of a BST and a key, delete the node with given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
    - Search for a node to remove.
    - If the node is found, delete the node.

Example 1:
    - Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
    - Output: [5, 4, 6, 2, null, null, 7]
    - Explanation: Given key to delete is 3. So we find the node with a value 3 and delete it.
    One valid answer is [5, 4, 6, 2, null, null, 7], shown in the above BST. Please notice that another
    valid answer is [5, 2, 6, null, 4, null, 7] and it's also accepted.

Example 2:
    - Input: root = [5, 3, 6, 2, 4, null, 7], key = 0
    - Output: [5, 3, 6, 2, 4, null, 7]
    - Explanation: The tree does not contain a node with value = 0

Example 3:
    - Input: root = [], key = 0
    - Output: []
    - Explanation: Empty Tree

    
UPI

    Understand:
        - There is cases where you need to consider when removing nodes with or without children.
            - Case 1: Node with no children (Leaf node).
            - Case 2: Node with only one child, left or right child.
            - Case 3: Node with both left/right children.
                - To solve Case 3, replacement value is needed to replace the deleted node.
                - The goal is to maintain the BST property after deletion.
                - In-Order Successor: The smallest node in the right subtree of the node to be deleted.
                    - Going to the right child of the node.
                    - From there, moving as far left as possible until you reach a node with no left child. This node is the
                        in-order successor.
                - Delete the In-order Successor
                    - 
        - Find a method to search for the nodes within the tree.


        Why use In-order Successor?
            - When deleting a node with two children, we replace the node's value with its in-order successor to preserve
            the BST property. The in-order successor is always greater than all the values in the node's left subtree and smaller
            than all the values in its right subtree.
    
    Plan:
        - 
    
'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # If the list is empty
        if not root:
            return root

        # Search for a node to delete
        if key > root.val:
            # Search the right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # Search the left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # Case 1: Node with no children (Leaf node)
            if not root.left and not root.right:
                return None
            
            # Case 2: Node with only one child, left or right child
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            # Case 3: Node with both left/right children
            pointer = root.right
            while pointer.left: # Find the min either from left or right subtree. Using in-order successor.
                pointer = pointer.left
            root.val = pointer.val
            # Delete the in-order sucessor.
            root.right = self.deleteNode(root.right, pointer.val)
        return root

def print_in_order(root: Optional[TreeNode]):
    if not root:
        return []
    return print_in_order(root.left) + [root.val] + print_in_order(root.right)

# Construct the tree as described in the example
#          50
#        /    \
#      30      70
#     /  \    /  \
#    20  40  60  80
#          \   \
#          45  65

root = TreeNode(50)
root.left = TreeNode(30, TreeNode(20), TreeNode(40, None, TreeNode(45)))
root.right = TreeNode(70, TreeNode(60, None, TreeNode(65)), TreeNode(80))

# Before deletion
original_tree = print_in_order(root)

# Delete node with value 50
solution = Solution()
root = solution.deleteNode(root, 50)

# After deletion
updated_tree = print_in_order(root)

print(original_tree)
print(updated_tree)