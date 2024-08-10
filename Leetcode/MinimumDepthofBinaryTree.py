'''

Given a binary tree, finds its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no left right children.

Example 1:
    - Input: root = [3, 9, 20, null, null, 15, 7]
    - Output: 2

'''


from collections import deque
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
        #return dfsHelper(root)

        def bfsHelper(root):
            
            queue = deque([root])
            level = 1 

            while queue:

                for _ in range(len(queue)):

                    current = queue.popleft()
                    if not current.left and not current.right:
                        return level
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)

                level = level + 1
            return level
        return bfsHelper(root)

