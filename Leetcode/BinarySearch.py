'''

704. Binary Search

Given an array of integer nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists. then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    - Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    - Output: 4
    - Explanation: 9 exists in nums and its index is 4

Example 2:
    - Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    - Output: -1
    - Explanation: 2 exists in nums and its index is 4


'''

class Solution:

    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target:
                # If the current middle value is larger than the target
                # the target must be on the left side.
                # Discard the right half by moving 'right' to 'middle - 1'.
                right = middle - 1
            
            elif nums[middle] < target:
                # If the current middle value is smaller than the target
                # the target must be on the right side.
                # Discard the left half by moving 'left' to 'middle + 1'.
                left = middle + 1

            else:
                # If the middle value matches the target, return the index.
                return middle
        
        return -1  # If the target is not found in the list.

sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 3))