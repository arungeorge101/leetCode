"""
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    #using string manipulation
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        flag = 0
        for i in range(len(s)):
            if(s[i] != s[(len(s)-1-i)]):
                flag = 1
        
        if(flag == 0):
            return True
        
        return False
    
    #without using string manipulation
    def isPalindromeInt(self, x: int) -> bool:

        newNum = 0
        if(x < 0):
            flag = 0
        else:
            cp = x
            while(cp > 0):
                newNum = (newNum * 10) + cp % 10
                cp = int(cp / 10)

        if(x == newNum):
            return True
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindromeInt(121))
