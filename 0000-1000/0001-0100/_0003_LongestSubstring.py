class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        solution = 1
        start = 0
        current = dict()
        for i,char in enumerate(s):
            if char in current and current[char]>=start:
                solution=max(solution, i-start)
                start = current[char]+1
            else:
                solution=max(solution, i-start+1)
            current[char]=i
        return solution

        