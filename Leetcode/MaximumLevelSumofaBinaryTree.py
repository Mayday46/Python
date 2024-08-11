


'''

1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, and the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

'''

from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            if not root:
                return {}
            
            reference, level = dict(), 1
            queue = deque([root])

            while queue:
                size = len(queue)

                for _ in range(size):
                    current = queue.popleft()
                    if level not in reference:
                        reference[level] = [current.val]
                    else:
                        reference[level].append(current.val)
                    
                    if current.left:
                        queue.append(current.left)
                    
                    if current.right:
                        queue.append(current.right)
                
                level += 1
            
            return reference

        lists = bfs(root)
        temp, res = float('-inf'), None

        for key, values in lists.items():
            currentSum = sum(values)

            if currentSum > temp:
                temp = currentSum
                res = key
                
        return res


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

solution = Solution()
print(solution.maxLevelSum(root))
