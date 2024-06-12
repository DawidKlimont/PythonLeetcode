class Solution:
    def minimumSum(self, num: int) -> int:
        digits=[]
        while num!=0:
            digits.append(num%10)
            num = num//10

        digits.sort()
        total_sum=0
        for i in range(1,len(digits),2):
            total_sum = total_sum*10
            total_sum += digits[i-1]+digits[i]

        return total_sum

print(Solution().minimumSum(2932))