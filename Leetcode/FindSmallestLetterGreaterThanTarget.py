'''

744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greather than target.
If such a character does not exist, return the first character in letters.

Example 1:
    - Input: letters = ["c", "f", "j"], target = "a"
    - Output: "c"
    - Explanation: The smallest character that is lexicographically greater than 'a' in letters
    is 'c'.


'''

class Solution:
    def nextGreatestLetter(self, nums: list[str], target: str) -> str:
        left, right = 0, len(nums) - 1
        
        # Binary search to find the smallest letter greater than the target
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] > target:
                right = middle - 1  # Move left, but this could still be the answer
            else:
                left = middle + 1  # Move right, because nums[middle] <= target
        
        # Check if left has gone out of bounds (i.e., no valid letter greater than target)
        if left >= len(nums):
            return nums[0]  # Return the first letter because of circular condition
        
        # Otherwise, return the letter at the position found
        return nums[left]