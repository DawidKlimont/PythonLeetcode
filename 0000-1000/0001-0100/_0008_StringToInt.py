class Solution:
    def myAtoi(self, s: str) -> int:
        solution = 0
        started = False
        is_negative = False
        
        for char in s:
            if started:
                if char.isdigit():
                    solution*=10
                    solution+=int(char)
                else:
                    break
            else:
                match char:
                    case "-":
                        is_negative = True
                        started = True
                    case "+":
                        started = True
                    case char if char.isdigit():
                        solution = int(char)
                        started = True
                    case char if char != " ":
                        print(char)
                        return solution

        limit = 2**31
        if is_negative:
            if solution <= limit:
                return -solution
            else:
                return -limit
        else:
            if solution <= limit-1:
                return solution
            else:
                return limit-1
    
print(Solution().myAtoi("1337c0d3"))