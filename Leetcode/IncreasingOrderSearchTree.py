'''

897. Increasing Order Search Tree

Given the root of a binary search tree. rearrange the tree in-order so that the leftmost node
in the tree is now the root of the tree, and every node has not left child and only one right child.

Example 1:
    - Input: root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
    - Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7, null, 8, null, 9]

Example 2:
    -Input root = [5, 1, 7]
    - Output: [1, null, 5, null, 7]


'''
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = inorder(root)
        size = len(nodes)
        rootNode = TreeNode(nodes[0])
        current = rootNode
        for i in range(1, size):
            current.right = TreeNode(nodes[i])
            current = current.right
        return rootNode


def inorder(root, res = None):
    if res is None:
        res = []
    
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)
    
    return res
