class Solution:
    def reverse(self, x: int) -> int:
        solution = 0
        limit = (2**31)
        num = abs(x)

        while num != 0:
            #check if next step would land outside 32 bit range
            if solution > limit/10:
                return 0
            else:
                solution *= 10
                solution += num%10
                num = num//10
        
        if x<0:
            return -solution 
        else:
            return solution 
        
print(Solution().reverse(-123))