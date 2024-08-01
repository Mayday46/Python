'''

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values


Example1:

Input: root = [1, null, 2, 3]
Output: [1, 3, 2]

Example2:

Input: root = []
Output: []

Example2:

Input: root = [1]
Output: [1]

'''
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    
    result = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        result.append(root.val)
        helper(root.right)
    helper(root)
    return result