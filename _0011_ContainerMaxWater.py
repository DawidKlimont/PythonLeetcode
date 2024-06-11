from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1

        while left != right:
            cur_water = (right-left) * min(height[left], height[right])
            max_water = max(max_water, cur_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))