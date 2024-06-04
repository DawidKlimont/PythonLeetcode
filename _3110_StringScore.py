def scoreOfString(s: str) -> int:
    index = 0
    solution = 0
    while index < len(s)-1:
        solution += abs(ord(s[index])-ord(s[index+1]))
        index += 1
    return solution
    
print(scoreOfString("hello"))