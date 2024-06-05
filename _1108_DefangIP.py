class Solution:
    def defangIPaddr(self, address: str) -> str:
        solution=""
        for char in address:
            if char == '.':
                solution += "[.]"
            else:
                solution += char
        return solution

print(Solution().defangIPaddr("1.1.1.1"))