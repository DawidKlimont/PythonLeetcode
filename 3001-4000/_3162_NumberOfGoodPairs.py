from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        solution = 0
        for num1 in nums1:
            counter=0
            for num2 in nums2:
                if num1%(num2*k)==0:
                    counter+=1
            solution+=counter
        return solution

print(Solution().numberOfPairs([1,3,4],[1,3,4],1))