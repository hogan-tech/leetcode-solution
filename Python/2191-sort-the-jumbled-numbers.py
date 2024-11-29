# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        indexList = []
        tempList = []
        originalList = list(nums)
        for i in range(len(nums)):
            indexList.append(i)
            tempNum = 0
            for digit in str(nums[i]):
                tempNum = 10 * tempNum + mapping[int(digit)]
                nums[i] //= 10
            tempList.append(tempNum)
        ans = []
        for pair in sorted(zip(tempList, indexList)):
            ans.append(originalList[pair[1]])
        return ans


mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(Solution().sortJumbled(mapping, nums))
