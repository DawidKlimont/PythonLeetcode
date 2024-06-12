from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered=[]
        for i in heights:
            ordered.append(i)
        ordered.sort()

        solution=0
        for i in range(len(heights)):
            if heights[i]!=ordered[i]:
                solution+=1
        return solution

print(Solution().heightChecker([1,1,4,2,1,3]))