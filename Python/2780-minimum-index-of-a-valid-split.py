# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        firstCounter = defaultdict(int)
        seconfCounter = defaultdict(int)
        for num in nums:
            firstCounter[num] += 1
        for i, num in enumerate(nums):
            firstCounter[num] -= 1
            seconfCounter[num] += 1
            if seconfCounter[num] * 2 > i + 1 and firstCounter[num] * 2 > len(nums) - i - 1:
                return i
        return -1


nums = [1, 2, 2, 2]
print(Solution().minimumIndex(nums))
nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
print(Solution().minimumIndex(nums))
nums = [3, 3, 3, 3, 7, 2, 2]
print(Solution().minimumIndex(nums))
