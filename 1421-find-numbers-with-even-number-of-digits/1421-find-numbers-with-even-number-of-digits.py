# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


nums = [12, 345, 2, 6, 7896]
print(Solution().findNumbers(nums))
nums = [555, 901, 482, 1771]
print(Solution().findNumbers(nums))
