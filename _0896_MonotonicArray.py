from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        start = -1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                start = i
                break
        
        if start == -1:
            return True

        if nums[start]<nums[start+1]:
            for i in range(start+1, len(nums)-1):
                if not (nums[i]<=nums[i+1]):
                    return False
        else:
            for i in range(start+1, len(nums)-1):
                if not (nums[i]>=nums[i+1]):
                    return False
        return True
    
print(Solution().isMonotonic([1,2,2,3]))