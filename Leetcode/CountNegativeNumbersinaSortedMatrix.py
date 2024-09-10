'''

1351. Count Negative Numbers in a Sorted Matrix

'''

class Solution:

    def search(self, target: list[int]) -> int:
        left, right = 0, len(target) - 1
        count = 0

        while left <= right:
            middle = (left + right) // 2

            if target[middle] >= 0:
                left = middle + 1
            else:
                # target[middle] < 0
                right = middle - 1
                count = len(target) - middle
        return count

    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for eachRow in range(len(grid)):
            count += self.search(grid[eachRow])
        return count


        
    def countNegativesBruteForce(self, grid: list[list[int]]) -> int:
        negative = 0
        for row in range(len(grid)):
            for each in range(len(grid[row])):
                if grid[row][each] < 0:
                    negative += 1
        
        return negative

sol = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(grid))