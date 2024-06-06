from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
            solution=0
            for l in accounts:
                solution=max(solution, sum(l))
            return solution

print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))