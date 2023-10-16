import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for key, value in collections.Counter(nums).items():
            if (value > len(nums)/3):
                result.append(key)
        return result


nums = [1, 2]
print(Solution().majorityElement(nums))
