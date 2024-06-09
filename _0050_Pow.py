class Solution:
    def myPow(self, x: float, n: int) -> float:
        #exponent negative we divide x else multiply x
        if n < 0:
            potenz = 1/x
        else:
            potenz = x

        #look at bits of n as (x * x**2 * x**4 * x**8 * ...)(<-lil endian)
        solution = 1
        n = abs(n)
        while n!=0:
            if 1&n:
                solution=solution*potenz
            potenz = potenz*potenz
            n=n>>1
        return solution

print(Solution().myPow(2.0,-2))