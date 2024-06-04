def defangIPaddr(address: str) -> str:
    solution=""
    for char in address:
        if char == '.':
            solution += "[.]"
        else:
            solution += char
    return solution

print(defangIPaddr("1.1.1.1"))