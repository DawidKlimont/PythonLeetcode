class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s

        longest_start = 0
        longest_end = 0


        for i in range(len(s)-1):
            last_pali=0
            for j in range( 1,min(i+1,len(s)-i) ):
                if s[i+j] == s[i-j]:
                    last_pali=j
                else: 
                    break
            if (i+last_pali)-(i-last_pali)>longest_end-longest_start:
                longest_start = i-last_pali
                longest_end = i+last_pali

            if s[i] == s[i+1]:
                last_pali=0
                for j in range( 1,min(i+1,len(s)-i-1) ):
                    if s[i+j+1] == s[i-j]:
                        last_pali=j
                    else: 
                        break
                if (i+1+last_pali)-(i-last_pali)>longest_end-longest_start:
                    longest_start = i-last_pali
                    longest_end = i+1+last_pali  

        return s[longest_start:longest_end+1]