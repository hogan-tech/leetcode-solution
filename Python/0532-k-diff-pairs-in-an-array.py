from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            if left == right or (nums[right] - nums[left]) < k:
                right += 1
            elif (nums[right] - nums[left]) > k:
                left += 1
            else:
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left-1]):
                    left += 1

        return result


nums = [3, 1, 4, 1, 5]
k = 2

print(Solution().findPairs(nums, k))
