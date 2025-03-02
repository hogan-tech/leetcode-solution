# time complexity: O(n^2)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        for i in range(len(nums) - k + 1):
            uniqueNums = set(nums[i: i + k])
            for num in uniqueNums:
                freq[num] += 1
        result = -1
        for key, value in freq.items():
            if value == 1:
                result = max(result, key)
        return result


nums = [3, 9, 2, 1, 7]
k = 3
print(Solution().largestInteger(nums, k))
nums = [3, 9, 7, 2, 1, 7]
k = 4
print(Solution().largestInteger(nums, k))
nums = [0, 0]
k = 1
print(Solution().largestInteger(nums, k))  # -1
nums = [0, 0]
k = 2
print(Solution().largestInteger(nums, k))  # 0
