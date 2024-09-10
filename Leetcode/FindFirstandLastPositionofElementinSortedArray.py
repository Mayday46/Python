'''

34. Find First and Last Position of Element in Sorted Array


'''

class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # Narrow the search to the left half
            else:
                left = mid + 1
            if nums[mid] == target:
                first = mid  # Record the potential first occurrence
        return first


    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1  # Narrow the search to the right half
            else:
                right = mid - 1
            if nums[mid] == target:
                last = mid  # Record the potential last occurrence
        return last


    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if not nums or len(nums) == 0:
            return [-1, -1]
        
        first = self.searchLeft(nums, target)
        last = self.searchRight(nums, target)

        return [first, last]

solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target))