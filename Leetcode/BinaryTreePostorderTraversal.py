'''

145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes's values.

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        
        res = []

        def postorder(root):
            if not root:
                return []
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        
        postorder(root)
        
        return res