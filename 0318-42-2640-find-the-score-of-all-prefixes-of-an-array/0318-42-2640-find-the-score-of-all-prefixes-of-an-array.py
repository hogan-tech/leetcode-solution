# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        convert = []
        tempMax = 0
        for num in nums:
            tempMax = max(tempMax, num)
            convert.append(tempMax + num)

        prefix = [convert[0]]
        for i in range(1, len(convert)):
            prefix.append(prefix[i-1] + convert[i])

        return prefix


nums = [2, 3, 7, 5, 10]
print(Solution().findPrefixScore(nums))
nums = [1, 1, 2, 4, 8, 16]
print(Solution().findPrefixScore(nums))
