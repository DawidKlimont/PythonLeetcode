class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stored = dict()
        seen = set()
        copy = ""
        for i,char in enumerate(s):
            if not char in stored:
                if t[i] in seen:
                    return False
                seen.add(t[i])
                stored[char]=t[i]
            copy+=stored[char]
        return copy == t
                
print(Solution().isIsomorphic("egg", "add"))