class Solution:
    def scoreOfString(self, s: str) -> int:
        solution = 0
        for i in  range(0,len(s)-1):
            solution += abs(ord(s[i])-ord(s[i+1]))
        return solution
    
print(Solution().scoreOfString("hello"))