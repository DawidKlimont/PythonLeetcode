from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_height_col = [0]*len(grid)
        max_height_row = [0]*len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_height_col[i] = max(max_height_col[i], grid[i][j])
                max_height_row[j] = max(max_height_row[j], grid[i][j])

        solution = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                solution += min(max_height_col[i],max_height_row[j]) - grid[i][j]
        return solution

print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
        