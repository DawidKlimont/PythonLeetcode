from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
        solution=0
        for l in accounts:
            solution=max(solution, sum(l))
        return solution

print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))