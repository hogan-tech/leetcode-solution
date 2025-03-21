# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numIdx = defaultdict(int)
        for i, num in enumerate(nums):
            numIdx[num] = i

        for oldNum, newNum in operations:
            currIdx = numIdx[oldNum]
            del numIdx[oldNum]
            numIdx[newNum] = currIdx

        for key, val in numIdx.items():
            nums[val] = key

        return nums


nums = [1, 2, 4, 6]
operations = [[1, 3], [4, 7], [6, 1]]
print(Solution().arrayChange(nums, operations))
nums = [1, 2]
operations = [[1, 3], [2, 1], [3, 2]]
print(Solution().arrayChange(nums, operations))
