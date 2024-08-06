'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is node with no children.


'''

from typing import Optional


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.right = right
        self.left = left



class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        res = []

        def dfs(root, path=[]):
            if not root:
                return
            
            # Include the current node in the path
            path.append(str(root.val))
            
            # If it's a leaf node, join the path and add it to results
            if not root.left and not root.right:
                res.append(" -> ".join(path))
            else:
                # Continue to traverse left and right subtrees
                dfs(root.left, path)
                dfs(root.right, path)

            # Backtrack: remove the current node from the path
            path.pop()
        dfs(root)
        return res

# Construct the tree for Example 1
#       1
#      / \
#     2   3
#      \
#       5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()
output = solution.binaryTreePaths(root)
print(output)
