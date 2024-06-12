from typing import List


class Solution:
    def findWordsContaining(words: List[str], x: str) -> List[int]:
        solution = []
        for i,w in enumerate(words):
            if x in w:
                solution.append(i)
        return solution

print(Solution().findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))