from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        solution=0
        for i in hours:
            if i>=target:
                solution+=1
        return solution
    
print(Solution().numberOfEmployeesWhoMetTarget([0,1,2,3,4],2))