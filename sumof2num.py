"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
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