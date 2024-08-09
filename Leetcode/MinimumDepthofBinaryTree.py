'''

Given a binary tree, finds its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no left right children.


'''


from typing import Optional


class TreeNode:

    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def dfsHelper(node, currentDepth = 1):

            if not node:
                return
            
            if not node.left and not node.right:
                return currentDepth
            
            left = dfsHelper(node.left, currentDepth + 1)
            right = dfsHelper(node.right, currentDepth + 1)

            return min(left, right)
        
        return dfsHelper(root)

