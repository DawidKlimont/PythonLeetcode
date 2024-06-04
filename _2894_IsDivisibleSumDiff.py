def differenceOfSums(n: int, m: int) -> int:
    index = 1
    num1 = 0
    num2 = 0
    while index <= n:
        if index%m == 0:
            num2+=index
        else:
            num1+=index
        index +=1
    return num1-num2

print(differenceOfSums(10,3))