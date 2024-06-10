from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        solution = 0
        for sentence in sentences:
            solution = max(solution, len(sentence.split()))
        return solution
    
print(Solution().mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))