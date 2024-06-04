from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    hashmap = {}
    solution = 0
    for i in nums:
        if i in hashmap:
            solution += hashmap[i]
            hashmap[i] += 1

        else:
            hashmap[i] = 1
    return solution

print(numIdenticalPairs([1,2,3,1,1,3]))