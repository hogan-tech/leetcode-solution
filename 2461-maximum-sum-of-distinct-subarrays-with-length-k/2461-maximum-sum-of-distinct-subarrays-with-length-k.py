# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        freq = defaultdict(int)
        count = 0
        for i in range(k):
            freq[nums[i]] += 1
            count += nums[i]
        if len(freq) == k:
            result = count

        for i in range(k, len(nums)):
            freq[nums[i]] += 1
            count += nums[i]
            freq[nums[i-k]] -= 1
            count -= nums[i-k]
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]
            if len(freq) == k:
                result = max(result, count)
        return result


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(Solution().maximumSubarraySum(nums, k))
nums = [4, 4, 4]
k = 3
print(Solution().maximumSubarraySum(nums, k))
nums = [1, 1, 1, 7, 8, 9]
k = 3
print(Solution().maximumSubarraySum(nums, k))
