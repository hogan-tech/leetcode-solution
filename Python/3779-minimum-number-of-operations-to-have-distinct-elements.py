# time complexity: O(n)
# space complexity: O(n)
from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dup = sum(1 for v in freq.values() if v >= 2)
        if dup == 0:
            return 0
        result = 0
        i = 0
        n = len(nums)
        while i < n:
            result += 1
            for _ in range(3):
                if i >= n:
                    break
                x = nums[i]
                freq[x] -= 1
                if freq[x] == 1:
                    dup -= 1
                i += 1
            if dup == 0:
                break
        return result


nums = [3, 8, 3, 6, 5, 8]
print(Solution().minOperations(nums))
nums = [2, 2]
print(Solution().minOperations(nums))
nums = [4, 3, 5, 1, 2]
print(Solution().minOperations(nums))
