'''

102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level)

Example 1:
    - Input: root = [3, 9, 20, null, null, 15, 7]
    - Output: [[3], [9, 20], [15, 7]]

Example 2:
    - Input: root = [1]
    - Output: [[1]]

Example 3:
    - Input: root = []
    - Output: []



UPI

Understand:
    - Breadth First Search.

Plan:
    - How to stop at the end of each level?
        - For loop
    
'''
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            # If the root is None, return an empty list, as there are no nodes to traverse.
            return []
        
        res = []
        # Initialize an empty list to store the final result, where each sublist contains nodes at each level.
        queue = deque([root])
        # Initialize a deque (double-ended queue) with the root node to start the BFS.

        while queue:
            # While there are still nodes to process in the queue:
            level = []
            # Initialize an empty list to store nodes at the current level.
            size = len(queue)
            # Determine the number of nodes at the current level (the current size of the queue).
            for i in range(size):
                # Iterate over all nodes at the current level.
                current = queue.popleft()
                # Pop the leftmost node from the queue to process it.
                level.append(current.val)
                # Add the value of the current node to the list representing this level.
                if current.left:
                    queue.append(current.left)
                    # If the current node has a left child, add it to the queue for the next level's processing.
                if current.right:
                    queue.append(current.right)
                    # If the current node has a right child, add it to the queue for the next level's processing.

            res.append(level)
            # After processing all nodes at the current level, add the list of this level's node values to the result.
        return res
        # Once all levels are processed and the queue is empty, return the final result.
    
#         19
#        /  \
#       7    25
#      /    /  \
#     5    22   71
#    /         /  \
#   6         30   96

node_6 = TreeNode(6)
node_30 = TreeNode(30)
node_96 = TreeNode(96)

# Intermediate nodes
node_5 = TreeNode(5, left=node_6)
node_22 = TreeNode(22)
node_71 = TreeNode(71, left=node_30, right=node_96)

# Parent nodes
node_7 = TreeNode(7, left=node_5)
node_25 = TreeNode(25, left=node_22, right=node_71)

# Root node
root = TreeNode(19, left=node_7, right=node_25)

solution = Solution()
print(solution.levelOrder(root))

