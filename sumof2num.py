"""
https://leetcode.com/problems/two-sum/
"""


from typing import List
class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        retList = []
        flag = 0
        for i in range(0, len(nums)):
            print("i = " + str(i))
            for j in range(i+1,len(nums)):
                print("j = " + str(j))
                if(nums[i] + nums[j] == target):
                    retList.append(i)
                    retList.append(j)
                    flag = 1
                if(flag == 1):
                    break
            if(flag == 1):
                    break
        return retList


if __name__ == "__main__":
    s = solution()
    print(s.twoSum())