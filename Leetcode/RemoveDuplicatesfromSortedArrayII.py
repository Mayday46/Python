


'''

80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element
appears at most twice. The relative order of the elemnts should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in
first part of the array nums. More formally, if there are k elements after removing the duplicates, the the first K elements
of nums should hold the final result. It does not matter what you leave beyond the first K elements.

Return k after placing the final result in the first K slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:
    - Input: nums = [1, 1, 1, 2, 2, 3]
    - Output: 5, nums = [1, 1, 2, 2, 3, _]
    - Explanation: Your function should return k = 5, with the first five elements for nums being 1, 1, 2, 2 and 3 respectively.
    It does not matter what you leave beyond the returned K (hence they are underscores).
'''
class Solution:
    # [0, 0, 0, 0, 1, 2, 2, 2, 3]
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        writer, count = 1, 1

        for reader in range(1, len(nums)):
            if nums[reader] == nums[reader - 1]:
                if count < 2:
                    count += 1
                    nums[writer] = nums[reader]
                    writer += 1
            else:
                count = 1
                nums[writer] = nums[reader]
                writer += 1
        
        return [writer, nums]

sol = Solution()
arr = [0, 0, 0, 0, 1, 2, 2, 2, 3]
res = sol.removeDuplicates(arr)
print(res)
