# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        freq = [0] * (len(nums) + 1)
        for num in nums:
            freq[min(len(nums), num)] += 1
        count = 0
        for i in range(len(nums), 0, -1):
            count += freq[i]
            if i == count:
                return i
        return -1


nums = [3, 5]
print(Solution().specialArray(nums))
