from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i,valueI in enumerate(nums):
        if valueI in hashmap:
            return [hashmap[valueI], i] 
        else:
            hashmap[target-valueI] = i
    return [-1]