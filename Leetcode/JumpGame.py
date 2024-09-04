'''

55. Jump Game

You are given an integer array


'''

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        back = len(nums) - 1

        for i in range(back, -1 , -1):
            steps = nums[i] + i # This is to check the steps can reach the goal
            if steps >= goal:
                goal = i
        
        return True if goal == 0 else False