from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        total = []
        for point in points:
            total.append(point[0])
        total.sort()
        solution = 0
        for i in range(len(total)-1):
            new_val=total[i+1]-total[i]
            solution = max(solution,new_val)
        return solution
    
print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))