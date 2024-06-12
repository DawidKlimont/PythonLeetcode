from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        solution = [first]
        for i in range(0,len(encoded)):
            solution.append(solution[i]^encoded[i])
        return solution
        
print(Solution().decode([6,2,7,3],4))