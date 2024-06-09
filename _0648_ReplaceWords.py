from typing import List


class TrieElement:
    def __init__(self):
        self.nextChar = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieElement()

    def insert(self, word: str):
        cur = self.root
        for char in word:
            if not char in cur.nextChar:
                cur.nextChar[char]=TrieElement()
            cur = cur.nextChar[char]
        cur.isEnd = True

    def finShortestPre(self, word:str):
        cur = self.root
        for i,char in enumerate(word):
            if cur.isEnd:
                return word[:i]  
            if not char in cur.nextChar:
                return word
            else:
                cur = cur.nextChar[char]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        text_split = sentence.split()
        for i,word in enumerate(text_split):
            text_split[i]=trie.finShortestPre(word)

        solution = text_split[0]
        for i in range(1,len(text_split)):
            solution+=" "+text_split[i]
        return solution
        

print(Solution().replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))