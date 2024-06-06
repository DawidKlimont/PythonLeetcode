from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,valueI in enumerate(nums):
            if valueI in hashmap:
                return [hashmap[valueI], i] 
            else:
                hashmap[target-valueI] = i
        return [-1]
    
print(Solution().twoSum([2,7,11,15],9))