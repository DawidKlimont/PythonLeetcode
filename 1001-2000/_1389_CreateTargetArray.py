from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
            solution = []
            for i in range(len(nums)):
                solution = solution[:index[i]] +[nums[i]]+ solution[index[i]:]
            return solution

print(Solution().createTargetArray([1,2,3,4,0],[0,1,2,3,0]))