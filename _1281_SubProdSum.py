class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        prod=1
        while n!=0:
            cur = n%10
            summ += cur
            prod *= cur
            n = int(n/10)
        return prod-summ
    
print(Solution().subtractProductAndSum(234))