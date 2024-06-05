from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    solution = []
    for i,w in enumerate(words):
        if x in w:
            solution.append(i)
    return solution

print(findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))