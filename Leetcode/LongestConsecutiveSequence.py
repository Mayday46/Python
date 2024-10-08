'''

128. Longest Consecutive Sequence

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # Return 0 if the list is empty
            return 0
        
        num_set = set(nums)  # Create a set from the list
        longest_streak = 0
        
        for num in num_set:
            # Only start counting from numbers that are the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak