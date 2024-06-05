from typing import List


def findArray(pref: List[int]) -> List[int]:
    prev=pref[0]
    for i in range(1, len(pref)):
        temp=pref[i]
        pref[i]=pref[i]^prev
        prev=temp
    return pref

print(findArray([5,2,0,3,1]))