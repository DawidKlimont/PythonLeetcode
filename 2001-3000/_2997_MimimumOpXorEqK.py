from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #generate XOR of nums
        xor = 0
        for num in nums:
            xor = xor^num

        #get differing bits
        diff = xor^k

        #count amount of bits set to 1 -> solution
        solution = 0
        while diff!=0:
            solution+=(diff&1)
            diff=diff>>1
        return solution
    
print(Solution().minOperations([2,1,3,4],1))