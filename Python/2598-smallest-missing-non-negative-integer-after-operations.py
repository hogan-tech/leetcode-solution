# time complexity: O(n)
# space complexity: O(k)
from typing import Counter, List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = Counter(x % value for x in nums)
        result = 0
        while counter[result % value] > 0:
            counter[result % value] -= 1
            result += 1
        return result


nums = [1, -10, 7, 13, 6, 8]
value = 5
print(Solution().findSmallestInteger(nums, value))
nums = [1, -10, 7, 13, 6, 8]
value = 7
print(Solution().findSmallestInteger(nums, value))
