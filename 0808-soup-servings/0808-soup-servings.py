from functools import lru_cache
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n/25)

        @lru_cache(None)
        def calculate_dp(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            return (calculate_dp(i-4, j) + calculate_dp(i-3, j-1) +
                    calculate_dp(i-2, j-2) + calculate_dp(i-1, j-3)) / 4.0

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0
        return calculate_dp(m, m)
