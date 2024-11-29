# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        countList = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    countList[i] = max(countList[i], countList[j] + 1)
        return max(countList)


nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))
