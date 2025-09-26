# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums) - 1, -1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count


nums = [2, 2, 3, 4]
print(Solution().triangleNumber(nums))
nums = [4, 2, 3, 4]
print(Solution().triangleNumber(nums))
