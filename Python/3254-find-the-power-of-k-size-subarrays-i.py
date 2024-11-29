# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def resultPower(currIdx: int):
            for i in range(1, k):
                if nums[currIdx + i] != nums[currIdx + i-1] + 1:
                    return -1
            return max(nums[currIdx:currIdx + k])
        result = []
        for i in range(len(nums) - k + 1):
            result.append(resultPower(i))
        return result


nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
print(Solution().resultsArray(nums, k))
nums = [2, 2, 2, 2, 2]
k = 4
print(Solution().resultsArray(nums, k))
nums = [3, 2, 3, 2, 3, 2]
k = 2
print(Solution().resultsArray(nums, k))
