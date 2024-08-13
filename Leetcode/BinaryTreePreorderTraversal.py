'''
144. Binary Tree Preorder Traversal.

Given the root of a binary tree, return the preoder traversal of its nodes' values.

Example 1:
    - Input: root = [1, null, 2, 3]
    - Output: [3, 2, 1]

'''

from typing import Optional


class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # Preorder Traversal
        # 1. Visit the node first
        # 2. Traverse left
        # 3. Traverse right
        res = []

        def preorder(root):
            if not root:
                return []
            
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return res