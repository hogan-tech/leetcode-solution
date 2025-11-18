# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        countArray = [0] * (length + 1)
        same, miss = 0, 0
        for num in nums:
            countArray[num] += 1

        for i in range(1, len(countArray)):
            if countArray[i] == 2:
                same = i
            if countArray[i] == 0:
                miss = i

        return [same, miss]


nums = [1, 1]
print(Solution().findErrorNums(nums))
