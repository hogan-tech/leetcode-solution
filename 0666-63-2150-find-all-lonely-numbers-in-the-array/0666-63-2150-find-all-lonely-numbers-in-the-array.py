# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = []
        for key, count in freq.items():
            if key + 1 in freq:
                continue
            if key - 1 in freq:
                continue
            if count == 1:
                result.append(key)
        return result


nums = [10, 6, 5, 8]
print(Solution().findLonely(nums))
nums = [1, 3, 5, 3]
print(Solution().findLonely(nums))
