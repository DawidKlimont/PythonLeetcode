class Solution:
    def romanToInt(self, s: str) -> int:
        romans = dict({
        "I":1,"X":10,"C":100,"M":1000,
        "V":5,"L":50,"D":500
        })
        solution=0
        for i,c in enumerate(s):
            if c=="I" and i+1<len(s) and (s[i+1]=="V" or s[i+1]=="X"):
                solution-=romans[c]
            elif c=="X" and i+1<len(s) and (s[i+1]=="L" or s[i+1]=="C"):
                solution-=romans[c]
            elif c=="C" and i+1<len(s) and (s[i+1]=="D" or s[i+1]=="M"):
                solution-=romans[c]
            else:
                solution+=romans[c]
        return solution
print(Solution().romanToInt("MCMXCIV"))