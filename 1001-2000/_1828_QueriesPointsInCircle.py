from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        solution=[]
        for circle in queries:
            count = 0
            for point in points:
                if (point[0]-circle[0])**2 + (point[1]-circle[1])**2 <= circle[2]**2:
                    count+=1
            solution.append(count)

        return solution
print(Solution().countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))