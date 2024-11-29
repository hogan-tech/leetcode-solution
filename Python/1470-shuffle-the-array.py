from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(Solution().shuffle(nums, n))
