"""
https://leetcode.com/problems/roman-to-integer/
"""

from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        strLen = len(s)
        skip = 0
        for i in range(strLen):
            print("loop :" + str(i))
            print("str :" + s[i])
            if( i !=0 and i == skip):
                continue
            if(s[i] == "I"):
                if(i != strLen-1 and s[i+1] == "V"):
                    num = num + 4
                    skip = i + 1
                elif(i != strLen-1 and s[i+1] == "X"):
                    num = num + 9
                    skip = i + 1
                else:
                    num = num + 1
            elif (s[i] == "V"):
                num = num + 5
            elif (s[i] == "X"):
                if(i != strLen-1 and s[i+1] == "L"):
                    num = num + 40
                    skip = i + 1
                elif(i != strLen-1 and s[i+1] == "C"):
                    num = num + 90
                    skip = i + 1
                else:
                    num = num + 10
            elif (s[i] == "L"):
                num = num + 50
            elif (s[i] == "C"):
                if(i != strLen-1 and s[i+1] == "D"):
                    num = num + 400
                    skip = i + 1
                elif(i != strLen-1 and s[i+1] == "M"):
                    num = num + 900
                    skip = i + 1
                else:
                    num = num + 100
            elif (s[i] == "D"):
                num = num + 500
            elif (s[i] == "M"):
                num = num + 1000

        return num

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))