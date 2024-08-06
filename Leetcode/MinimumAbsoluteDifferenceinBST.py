'''

530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the
values of any two different nodes in the tree.

Example 1:
    - Input: root = [4, 2, 6, 1, 3]
    - Output: 1


Example 2:
    - Input: root = [1, 0, 48, null, null, 12, 49]
    - Output: 1




'''


from typing import Optional


class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        traversalList = inorder_traversal(root)
        minimum = float('inf')
        for i in range(1, len(traversalList)):
            minimum = min(minimum, traversalList[i] - traversalList[i - 1])
        
        return minimum
        


def inorder_traversal(root, res = None):
    if res is None:
        res = []
    
    if root:
        inorder_traversal(root = root.left, res = res)
        res.append(root.val)
        inorder_traversal(root = root.right, res = res)
    return res

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6)
print(inorder_traversal(root))

solution = Solution()

print(solution.getMinimumDifference(root))