# time complexity: O(n^3)
# space complexity: O(n^2)
from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            return min(
                (values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)


values = [1, 2, 3]
print(Solution().minScoreTriangulation(values))
values = [3, 7, 4, 5]
print(Solution().minScoreTriangulation(values))
values = [1, 3, 1, 4, 1, 5]
print(Solution().minScoreTriangulation(values))
