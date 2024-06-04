from typing import List


def finalValueAfterOperations( operations: List[str]) -> int:
    solution = 0
    for op in operations:
        if op[1]=="+":
            solution+=1
        else:
            solution-=1
    return solution

print(finalValueAfterOperations(["--X","X++","X++"]))
    