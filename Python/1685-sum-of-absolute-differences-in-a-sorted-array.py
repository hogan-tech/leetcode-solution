# time complexity: O(1)
# space complexity: O(n)
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        suffixSum = sum(nums)
        prefixSum = 0
        res = []
        for i, num in enumerate(nums):
            res.append(i * num + suffixSum - prefixSum - (len(nums) - i) * num)
            prefixSum += num
            suffixSum -= num
        return res


nums = [1, 4, 6, 8, 10]
print(Solution().getSumAbsoluteDifferences(nums))
