class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix_mirror = ""
        index = -1
        for i,c in enumerate(word):
            prefix_mirror = c+prefix_mirror
            if c == ch:
                index = i+1
                break
        if index != -1:
            return prefix_mirror + word[index:] 
        else:
            return word
print(Solution().reversePrefix("abcdefd","d"))