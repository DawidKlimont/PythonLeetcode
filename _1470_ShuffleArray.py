from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    solution = []
    for i in range(0, n):
        solution.append(nums[i])
        solution.append(nums[i+n])
    return solution

print(shuffle([2,5,1,3,4,7],3))