# time complexity: O(n^2)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            items = list(Counter(nums[i:i+k]).items())
            items.sort(key=lambda item: (item[1], item[0]), reverse=True)

            tempSum = 0
            for j in range(min(x, len(items))):
                tempSum += items[j][0] * items[j][1]

            ans.append(tempSum)

        return ans


nums = [2, 5, 3, 5, 1]
k = 2
x = 1
print(Solution().findXSum(nums, k, x))
