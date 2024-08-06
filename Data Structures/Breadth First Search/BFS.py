from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''

If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue

'''


'''

Breadth First Search
    - Given a binary tree, breadth first search traverses nodes higher up in the tree (closest to the root) first. It is
    preferred when you expected the solution to be closer to the root. It also explores nodes level by level, from left to right.

    - BFS is commonly used for problems that require traversing by level.


'''


def breadth_first_search(root):
    if not root:
        return []
    
    queue = deque([root])  # Initialize queue with the root node
    visited = []

    while queue:
        current = queue.popleft()
        visited.append(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return visited


# Example tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Run BFS on the tree and print the output
print(breadth_first_search(root))
