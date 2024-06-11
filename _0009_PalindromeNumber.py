class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mirror = 0
        copy = x
        while copy != 0:
            mirror *= 10
            mirror += copy%10
            copy = copy//10
        return mirror == x
print(Solution().isPalindrome(121))