from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 0 if nums[i + 1] else 1
                nums[i + 2] = 0 if nums[i + 2] else 1
                count += 1

        return count if nums.count(0) == 0 else -1


nums = [0, 1, 1, 1, 0, 0]
print(Solution().minOperations(nums))
nums = [0, 1, 1, 1]
print(Solution().minOperations(nums))
nums = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
print(Solution().minOperations(nums))
nums = [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
print(Solution().minOperations(nums))
