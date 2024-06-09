from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        else:
            hand.sort()
            length = int(len(hand)/groupSize)

            for i in range(0,length):
                cur=hand[0]
                curSize=1

                hand.pop(0)
                index=0
                while curSize<groupSize:
                    if index == len(hand):
                        return False
                    if cur+1 == hand[index]:
                        cur = hand[index]
                        hand.pop(index)
                        curSize+=1
                    elif cur+1 < hand[index]:
                        print(groupSize)
                        print(curSize)
                        return False
                    else:
                        index+=1
            return True
        
print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8],3))