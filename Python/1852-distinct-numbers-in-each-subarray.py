# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(k):
            freq[nums[i]] += 1
        result = []
        result.append(len(freq))
        left = 0
        for right in range(k, len(nums)):
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            freq[nums[right]] += 1
            result.append(len(freq))
            left += 1
        return result


nums = [1, 2, 3, 2, 2, 1, 3]
k = 3
print(Solution().distinctNumbers(nums, k))
nums = [1, 1, 1, 1, 2, 3, 4]
k = 4
print(Solution().distinctNumbers(nums, k))
