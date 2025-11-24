from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3:
                count += 1
        return count


nums = [1, 2, 3, 4]
print(Solution().minimumOperations(nums))
nums = [3, 6, 9]
print(Solution().minimumOperations(nums))
