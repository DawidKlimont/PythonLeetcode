from typing import List
from time import process_time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,valueI in enumerate(nums):
            if valueI in hashmap:
                return [hashmap[valueI], i] 
            else:
                hashmap[target-valueI] = i
        return [-1]

def test(instace: Solution, iteration: int):
    start = process_time()
    percent_step = 34
    step_val = int(iteration/(100/percent_step))
    for i in range(iteration):
        if(i%step_val==0) and i>0:
           print(str(int((i/step_val)*percent_step))+"% done "+str(int(process_time()-start))+" seconds passed") 
        instance.twoSum([2,7,11,15],9)
    result = process_time()-start
    return result

instance = Solution()
print(instance.twoSum([2,7,11,15],9))

total = 0
iterations = 10_000_000
total+=test(instance,iterations)
print(str(total)+"s in total for "+str(iterations)+" iterations and "+str(total/(iterations))+"s avg")
