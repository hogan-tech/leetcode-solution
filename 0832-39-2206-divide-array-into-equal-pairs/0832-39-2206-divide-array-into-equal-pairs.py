# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for value in Counter(nums).values():
            if value % 2:
                return False
        return True


nums = [3, 2, 3, 2, 2, 2]
print(Solution().divideArray(nums))
nums = [1, 2, 3, 4]
print(Solution().divideArray(nums))
