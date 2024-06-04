def findPermutationDifference(s: str, t: str) -> int:
    hashmap = {}
    for i,char in enumerate(s):
        hashmap[char] = i

    solution = 0
    for i,char in enumerate(t):
        solution += abs(i-hashmap[char])
    return solution

print(findPermutationDifference("abc","bac"))