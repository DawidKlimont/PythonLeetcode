from typing import List

class SubrectangleQueries:
    rectangle: List[List[int]]

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j]=newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
    
def test():
    output=[None]
    sub = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
    output.append(sub.getValue(0,2))
    output.append(sub.updateSubrectangle(0,0,3,2,5))
    output.append(sub.getValue(0,2))
    output.append(sub.getValue(3,1))
    output.append(sub.updateSubrectangle(3,0,3,2,10))
    output.append(sub.getValue(3,1))
    output.append(sub.getValue(0,2))
    return output

print(test())