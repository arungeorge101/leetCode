"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List
class solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        print(nums3)
        
        arrLen = len(nums3)
        print(arrLen/2)

        if(arrLen%2 != 0):
            return nums3[int(arrLen/2)]
        else:
            print(nums3[int(arrLen/2)])
            print(nums3[int(arrLen/2)-1])
            median = ((nums3[int(arrLen/2)]+nums3[int(arrLen/2)-1])/2)
            return median


if __name__ == "__main__":
    s = solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))