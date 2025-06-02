# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        TOTAL = 1
        for num in nums:
            TOTAL *= num

        if TOTAL != target ** 2:
            return False

        mask = (1 << n) - 1
        for currMask in range(1, mask):
            if currMask == mask:
                continue
            prod = 1
            valid = True
            for i in range(n):
                if (currMask >> i) & 1:
                    prod *= nums[i]
                    if prod > target:
                        valid = False
                        break
            if valid and prod == target:
                return True

        return False


nums = [3, 1, 6, 8, 4]
target = 24
print(Solution().checkEqualPartitions(nums, target))
nums = [2, 5, 3, 7]
target = 15
print(Solution().checkEqualPartitions(nums, target))
