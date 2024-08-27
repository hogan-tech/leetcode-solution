# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j, count = 1, 1, 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1
            nums[j] = nums[i]
            j += 1
            i += 1

        del nums[j:]
        return len(nums)


nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
