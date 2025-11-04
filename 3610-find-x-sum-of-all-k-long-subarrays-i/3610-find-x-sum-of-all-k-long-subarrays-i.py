# time complexity: O(n^2 * klogk)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            items = list(Counter(nums[i:i+k]).items())
            items.sort(key=lambda item: (item[1], item[0]), reverse=True)

            tempSum = 0
            for j in range(min(x, len(items))):
                tempSum += items[j][0] * items[j][1]

            result.append(tempSum)

        return result


nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2
print(Solution().findXSum(nums, k, x))
nums = [3, 8, 7, 8, 7, 5]
k = 2
x = 2
print(Solution().findXSum(nums, k, x))
nums = [9, 2, 2]
k = 3
x = 3
print(Solution().findXSum(nums, k, x))
