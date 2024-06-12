from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        for i in nums:
            right+=i

        solution=[]
        for i in nums:
            right-=i
            solution.append(abs(left-right))
            left+=i
        return solution

print(Solution().leftRightDifference([10,4,8,3]))