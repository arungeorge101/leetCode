"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import List
class solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myStr = ""
        myList = []
        for i in range(len(s)):
            if not (s[i] in myStr):
                myStr = myStr + s[i]
            else:
                myList.append(myStr)
                ind = myStr.index(s[i])
                myStr = myStr[ind+1:] + s[i]
            
            if (i == (len(s)-1)):
                myList.append(myStr)

        length = 0
        for str1 in myList:
            if(len(str1) > length):
                length = len(str1)
                
        return length

if __name__ == "__main__":
    s = solution()
    print(s.lengthOfLongestSubstring("ckilbkd"))