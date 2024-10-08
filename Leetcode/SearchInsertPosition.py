'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime

'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                # if nums[middle] == target
                return middle
        
        return left

sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 2))