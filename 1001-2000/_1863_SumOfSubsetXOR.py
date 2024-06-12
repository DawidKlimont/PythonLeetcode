from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def Bs(index: int, solution: int) :
            if index == len(nums):
                return solution
            else:
                index_next=index+1
                solution_xor = solution^nums[index]
                return  Bs(index_next, solution)+Bs(index_next, solution_xor)

        return Bs(0,0)
    
print(Solution().subsetXORSum([1,3,2,3]))