'''

217. Contains Duplicate

Given an integer array nums, return True if any value appears at least twice in the array, and
return False if every element is distinct.

Example 1:
    - Input: nums = [1, 2, 3, 1]
    - Output: True

Example 2:
    - Input: nums = [1, 2, 3, 4]
    - Output: False

Example 3:
    - Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    - Output: True
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Brute force 
        # for i in range(len(nums)):
        #     counter = 0
        #     for j in range(i + 1, len(nums)):

        #         if nums[i] == nums[j]:
        #             return True
        
        # return False
        # Time Limit Exceeded
        table = set()
        for index in range(len(nums)):

            if nums[index] in table:
                return True
            else:
                table.add(nums[index])
        
        return False