from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = list(Counter(nums).values())
        max(freqs)
        ans = 0
        for freq in freqs:
            if freq == max(freqs):
                ans += freq
        return ans


nums = [1, 2, 2, 3, 1, 4]
print(Solution().maxFrequencyElements(nums))
