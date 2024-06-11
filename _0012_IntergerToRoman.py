class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            ["M", 1000],["CM", 900],["D", 500],["CD", 400],["C", 100],
            ["XC", 90],["L", 50],["XL", 40],["X", 10],["IX", 9],
            ["V", 5],["IV", 4],["I", 1]
        ]

        solution=""
        for element in romans:
            amount = num//element[1]
            solution += element[0]*amount
            num = num%element[1]
            
        return solution
    
print(Solution().intToRoman(3749))