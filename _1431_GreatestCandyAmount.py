from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        solution = []
        for i in candies:
            solution.append((greatest<=i+extraCandies))
        return solution
        
print(Solution().kidsWithCandies([2,3,5,1,3],3))