from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        solution=[]
        for i in nums:
            solution.append(nums[i])
        return solution

print(Solution().buildArray([0,2,1,5,3,4]))