from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        map = {}
        solution = []
        for index, size in enumerate(groupSizes):
            if size in map:
                map[size].append(index)
                if len(map[size])==size:
                    solution.append(map[size])
                    map.pop(size)
            else:
                if size > 1:
                    map[size] = [index]
                else:
                    solution.append([index])
        return solution

print(Solution().groupThePeople([3,3,3,3,3,1,3]))