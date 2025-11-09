# time complexity: O(n^3)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = float('inf')
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)-1):
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        result = min(result, abs(i - j) + abs(j - k) + abs(k - i))
        return result if result != float('inf') else -1


nums = [1, 2, 1, 1, 3]
print(Solution().minimumDistance(nums))
nums = [1, 1, 2, 3, 2, 1, 2]
print(Solution().minimumDistance(nums))
nums = [1]
print(Solution().minimumDistance(nums))
