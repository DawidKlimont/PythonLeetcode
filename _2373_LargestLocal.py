from typing import List


def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    solution = []
    for i in range(0,len(grid)-2):
        solution.append([])
        for j in range(0, len(grid[0])-2):
            value=0
            for k in range (0,3):
                for l in range (0,3):
                    value = max(value, grid[i+k][j+l])
            solution[i].append(value)
    return solution

print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))