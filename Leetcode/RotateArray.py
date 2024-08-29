'''

189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    - Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    - Output: [5, 6, 7, 1, 2, 3, 4]
    - Explanation:
        - Rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
        - Rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
        - Rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Example 2:
    - Input: nums = [-1, -100, 3, 99], k = 2
    - Output: [3, 99, -1, -100]
    - Explanation:
        - Rotate 1 steps to the right: [99, -1, -100, 3]
        - Rotate 2 steps to the right: [3, 99, -1, -100]


'''
class Solution:
    def BruteForcerotate(self, nums: list[int], k: int) -> None:

        # This approach is moving each element in the array k steps to the right.
        # Using extra memory approach.
        res = [1] * len(nums)
        for i in range(len(nums)):
            index = i + k
            if index < len(nums):
                res[index] = nums[i]
            else:
                index = (i + k) % len(nums)
                res[index] = nums[i]
        nums[:] = res
        return nums
    
    def rotate(self, nums: list[int], k: int) -> None:
        pivot = k % len(nums)
        nums[:] = nums[-pivot:] + nums[:-pivot]
        return nums