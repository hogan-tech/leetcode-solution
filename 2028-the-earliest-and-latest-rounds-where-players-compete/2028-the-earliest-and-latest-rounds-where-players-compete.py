# time complexity: O(n^4 * logn)
# space complexity: O(n^3)
from functools import lru_cache
from typing import List


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        @lru_cache(None)
        def dp(n: int, f: int, s: int):
            if f + s == n + 1:
                return (1, 1)

            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = float("inf"), float("-inf")
            nHalf = (n + 1) // 2

            if s <= nHalf:
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(nHalf, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                sPrime = n + 1 - s
                mid = (n - 2 * sPrime + 1) // 2
                for i in range(f):
                    for j in range(sPrime - f):
                        x, y = dp(nHalf, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        return [earliest, latest]


n = 11
firstPlayer = 2
secondPlayer = 4
print(Solution().earliestAndLatest(n, firstPlayer, secondPlayer))
n = 5
firstPlayer = 1
secondPlayer = 5
print(Solution().earliestAndLatest(n, firstPlayer, secondPlayer))
