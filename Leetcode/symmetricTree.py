'''

101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    - Input: root = [1, 2, 2, 3, 4, 4, 3]
    - Ouput: True

Example 2:
    - Input: root = [1, 2, 2, null, 3, null, 3]
    - Ouput: false

UPI

  Understand:
    - No need to check if the very top root node is symmetric. 
      - Symmetrical regardlesss the existence of the top root node.
    - Case 1: If root.left or root.right is none
      - If the root has no left and right, means that the tree is not Symmetrical due to un-even subtrees.
    - Case 2: If root.left and root.right is none.
      - Says that this node is alone.
    - Case 3: if the root.left.val != root.right.val
      - Symmetric requires nodes to have the same values.
  
  Plan:
    - Recursion
    - Check all three cases reursively
    
  
  Implement:
  
  

'''



from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            
            if not left and not right: # Case 1: If the root is null
                return True
            
            if not left or not right: # Case 2: If either left or right subtree is null, it not symmetric
                return False
            
            # Case 3: The root is not null, and it both has a left and right subtree
            if left.val != right.val:
                return False
            
            return (isMirror(left.left, right.right) and isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right) if root else True

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

solution = Solution()
print(solution.isSymmetric(root))  # Output: True
