from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #copy nums and sort
        nums_sorted=[]
        for i in nums:
            nums_sorted.append(i)
        nums_sorted.sort()

        #create dict and store first value
        cur = nums_sorted[0]
        seen = dict()
        seen[cur]=0

        #put all the searched values into the dict
        for i, num in enumerate(nums_sorted):
            if cur != num:
                seen[num]=i
                cur = num

        #create the solution with the values from the dict
        solution=[]
        for num in nums:
            solution.append(seen[num])
        return solution
    
print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))