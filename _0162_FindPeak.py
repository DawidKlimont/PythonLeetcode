from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        upper = len(nums)-1
        lower = 0
        while lower != upper:
            pivot = (lower+upper)//2
            value = nums[pivot]

            if pivot-1<0:
                left=float('-inf')
            else:
                left = nums[pivot-1]
            if pivot+1>=len(nums):
                right=float('-inf')
            else:
                right = nums[pivot+1]  

            if left<value and right<value:
                return pivot
            elif left>right:
                upper = pivot-1
            else:
                lower = pivot+1
        return lower
    
print(Solution().findPeakElement([1,2,3,1]))