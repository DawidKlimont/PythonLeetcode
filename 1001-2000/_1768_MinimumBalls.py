from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        left = [0]*n
        count_left = int(boxes[0])
        for i in range(1,n):
            left[i]=left[i-1]+count_left
            if boxes[i] == "1":
                count_left+=1

        right = [0]*n
        count_right = int(boxes[n-1])
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]+count_right
            if boxes[i] == "1":
                count_right+=1


        solution=[]
        for i in range(n):
            solution.append(left[i]+right[i])
        return solution

print(Solution().minOperations("001011"))