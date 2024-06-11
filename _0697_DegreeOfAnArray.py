from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        element_map = dict()
        seen = []
        sol_degree = 0


        for i,num in enumerate(nums):
            if num in element_map:
                degree = element_map[num][0]+1
                sol_degree = max(sol_degree, degree)
                element_map[num][0]=degree
                element_map[num][2]=i
            else:
                sol_degree = max(sol_degree, 1)
                element_map[num] = [1,i,i]
                seen.append(num)
        shortest = len(nums)
        for num in seen:
            cur = element_map[num]
            if cur[0]==sol_degree:
                cur_length = cur[2]-cur[1]+1
                shortest = min(shortest, cur_length)
        return shortest
    
print(Solution().findShortestSubArray([1,2,2,3,1]))