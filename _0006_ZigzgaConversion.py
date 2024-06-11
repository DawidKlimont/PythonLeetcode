class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #All start values
        zigzag = [""]*numRows
        counter = 0
        is_zag = False

        for char in s:
            #walking back up the rows (the zag in zigzag)
            if is_zag:
                zigzag[counter]+=char
                counter -= 1
                if counter <= 0:
                    is_zag = False
            #default case go down all rows
            elif not is_zag and counter < numRows:
                zigzag[counter]+=char
                counter+=1
            #reached end of rows decide what to do next
            else:
                #if zigging needs to be done and then do the first entry
                if numRows-2 > 0:
                    zigzag[numRows-2]+=char
                    if not numRows-3 <= 0:
                        counter = numRows-3
                        is_zag = True
                    else:
                        counter = 0
                #numRows <= 2 means no zagging after zigging
                else:
                    zigzag[0]+=char
                    counter = 1

        #assemble solution and return
        solution=""
        for word in zigzag:
            solution += word
        return solution

print(Solution().convert("PAYPALISHIRING",4))