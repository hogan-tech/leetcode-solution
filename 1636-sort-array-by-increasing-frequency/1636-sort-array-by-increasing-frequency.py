# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


nums = [1, 1, 2, 2, 2, 3]
print(Solution().frequencySort(nums))
