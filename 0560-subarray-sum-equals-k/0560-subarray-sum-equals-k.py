# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        dictionary = {0: 1}
        for num in nums:
            prefixSum += num
            if prefixSum - k in dictionary:
                count += dictionary[prefixSum - k]
            if prefixSum not in dictionary:
                dictionary[prefixSum] = 1
            else:
                dictionary[prefixSum] += 1
        return count


nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))
