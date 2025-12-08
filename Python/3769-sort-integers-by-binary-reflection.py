# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflect(x: int) -> int:
            b = bin(x)[2:]
            rb = b[::-1]
            return int(rb, 2)

        return sorted(nums, key=lambda x: (reflect(x), x))


nums = [4, 5, 4]
print(Solution().sortByReflection(nums))
nums = [3, 6, 5, 8]
print(Solution().sortByReflection(nums))
