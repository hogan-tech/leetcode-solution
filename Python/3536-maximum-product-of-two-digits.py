# time complexity: O(1)
# space complexity: O(1)
from heapq import heappop, heappush


class Solution:
    def maxProduct(self, n: int) -> int:
        numList = []
        for num in str(n):
            heappush(numList, -int(num))
        return heappop(numList) * heappop(numList)


n = 31
print(Solution().maxProduct(n))
n = 22
print(Solution().maxProduct(n))
n = 124
print(Solution().maxProduct(n))
n = 267
print(Solution().maxProduct(n))
