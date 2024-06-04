from typing import List


def getResults( queries: List[List[int]]) -> List[bool]:
    results = []
    blocks = [0]
    for query in queries:
        if query[0] == 1:
            index= 0
            dist = 0
            while index<len(blocks) and dist<query[1]:
                dist+=blocks[index]
                index+=1
            if dist>query[1]:
                value = query[1]-(dist-blocks[index-1])
                blocks = blocks[0:index-1]+[value, blocks[index-1]-value]+blocks[index:]
            else:
                blocks.append(query[1]-dist)
        elif query[0] == 2:
            fits = False
            dist = query[1]
            index = 0
            while index<len(blocks) and dist<blocks[index] and dist>=query[2]:
                dist -= blocks[index]
                print("test")
                if blocks[index]>=query[2]:
        
                    fits = True
                    break
                index+=1
            if dist>= query[2]:
                print(dist)
                fits = True
            results.append(fits)

    print(blocks)
    return results

print(getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
