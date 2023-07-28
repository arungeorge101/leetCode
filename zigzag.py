class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        j = 0
        col = int(len(s) / numRows)
        rows = numRows
        strArray = []
        strArray = ["" for x in range(rows)]
        k = rows - 1
        returnString = ""

        print("rows =  " + str(rows))
        print("cols =  " + str(col))

        for i in range(col):
            strArray[0] = strArray[0] + s[j]
            j = j + rows + (rows-2)
            
            if(k < len(s)):
                strArray[rows-1] = strArray[rows-1] + s[k]
                k = k + rows + (rows-2)

        for x in range(rows):
            returnString += strArray[x]
        return returnString

if __name__ == "__main__":
    s = Solution()
    print(s.convert("paypalishiring",3))
