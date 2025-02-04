# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitDict = defaultdict(list)
        for num in nums:
            tempSum = 0
            currNum = num
            while num > 0:
                num, digit = divmod(num, 10)
                tempSum += digit
            digitDict[tempSum].append(currNum)

        result = -1
        for _, numList in digitDict.items():
            if len(numList) < 2:
                continue
            numList.sort()
            result = max(result, numList[-1] + numList[-2])
        return result


nums = [18, 43, 36, 13, 7]
print(Solution().maximumSum(nums))
nums = [10, 12, 19, 14]
print(Solution().maximumSum(nums))
