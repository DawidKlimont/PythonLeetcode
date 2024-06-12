from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        solution = 0
        for i, num in enumerate(nums):
            set_bits = 0
            shifted = i
            while shifted > 0 :
                set_bits += shifted & 1
                shifted = shifted >> 1
            if set_bits==k:
                solution += num
        return solution

print(Solution().sumIndicesWithKSetBits([5,10,1,5,2],1))