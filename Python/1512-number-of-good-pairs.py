from collections import Counter
from typing import List


class Solution:
    def getSum(self, n: int) -> int:
        sum = 0
        for i in range(n):
            sum += i
        return sum

    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for key, value in Counter(nums).items():
            ans += self.getSum(value)
        return ans


nums = [1, 2, 3, 1, 1,1]
print(Solution().numIdenticalPairs(nums))
