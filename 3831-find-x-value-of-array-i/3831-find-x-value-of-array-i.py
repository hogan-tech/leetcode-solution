# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dpPrev = [0] * k

        for num in nums:
            x = num % k
            dpCurr = [0] * k
            dpCurr[x] += 1

            for i in range(k):
                temp = dpPrev[i]
                if temp:
                    dpCurr[(i * x) % k] += temp

            for i in range(k):
                result[i] += dpCurr[i]

            dpPrev = dpCurr

        return result


nums = [1, 2, 3, 4, 5]
k = 3
print(Solution().resultArray(nums, k))
nums = [1, 2, 4, 8, 16, 32]
k = 4
print(Solution().resultArray(nums, k))
nums = [1, 1, 2, 1, 1]
k = 2
print(Solution().resultArray(nums, k))
