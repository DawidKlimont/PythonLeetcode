class Solution:
    def balancedStringSplit(self, s: str) -> int:
        solution = 0
        counter_R = 0
        counter_L = 0

        for c in s:
            if c == "R":
                counter_R +=1
            else:
                counter_L +=1

            if counter_R == counter_L:
                solution+=1
                
        return solution

print(Solution().balancedStringSplit("RLRRLLRLRL"))