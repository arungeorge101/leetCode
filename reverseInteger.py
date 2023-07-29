"""
https://leetcode.com/problems/reverse-integer/description/
"""

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if(x < 0):
            negative = True
            x = x * -1

        str1 = str(x)
        print(str1)
        str2 = ""
        i = len(str1) -1
        
        while i >= 0:
            str2 = str2 + str1[i]
            i = i - 1
        
        rtnNum = int(str2)
        
        if(negative == True):
            rtnNum = rtnNum * -1
        
        if((rtnNum < -2147483648) or (rtnNum > 2147483647)):
            return 0 

        return rtnNum

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1534236469))