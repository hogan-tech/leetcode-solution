# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_right
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        banned.sort()
        banEnd = bisect_right(banned, n)
        banSet = set(banned[:banEnd])
        prefixSum = 0
        for num in range(1, n + 1):
            if num not in banSet:
                if prefixSum + num <= maxSum:
                    prefixSum += num
                    count += 1
                else:
                    break
        return count


banned = [1, 6, 5]
n = 5
maxSum = 6
print(Solution().maxCount(banned, n, maxSum))
banned = [1, 2, 3, 4, 5, 6, 7]
n = 8
maxSum = 1
print(Solution().maxCount(banned, n, maxSum))
banned = [11]
n = 7
maxSum = 50
print(Solution().maxCount(banned, n, maxSum))
