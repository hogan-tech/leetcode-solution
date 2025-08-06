# time complexity: O(n+klogn)
# space complexity: O(n)
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxTotalFruits(
        self, fruits: List[List[int]], startPos: int, k: int
    ) -> int:
        n = len(fruits)
        sumList = [0] * (n + 1)
        indices = [0] * n

        for i in range(n):
            sumList[i + 1] = sumList[i] + fruits[i][1]
            indices[i] = fruits[i][0]

        result = 0
        for x in range(k // 2 + 1):
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            result = max(result, sumList[end] - sumList[start])

            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            result = max(result, sumList[end] - sumList[start])

        return result


fruits = [[2, 8], [6, 3], [8, 6]]
startPos = 5
k = 4
print(Solution().maxTotalFruits(fruits, startPos, k))
fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
startPos = 5
k = 4
print(Solution().maxTotalFruits(fruits, startPos, k))
fruits = [[0, 3], [6, 4], [8, 5]]
startPos = 3
k = 2
print(Solution().maxTotalFruits(fruits, startPos, k))
