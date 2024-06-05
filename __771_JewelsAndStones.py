def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelSet = set()
    for c in jewels:
        jewelSet.add(c)
    solution = 0
    for c in stones:
        if c in jewelSet:
            solution+=1
    return solution

print(numJewelsInStones("aA","aAAbbbb"))
