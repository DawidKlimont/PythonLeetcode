from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        solution_sets = []
        for i in nums:
            inserted = False
            for sets in solution_sets:
                if not i in sets:
                    sets.add(i)
                    inserted = True
                    break
            if not inserted:
                next_sol = set()
                next_sol.add(i)
                solution_sets.append(next_sol)
        
        solution = []
        for sets in solution_sets:
            cur = []
            for s in sets:
                cur.append(s)
            solution.append(cur)
        return solution

print(Solution().findMatrix([1,3,4,1,2,3,1]))

        