# time complexity: O(l * m * n)
# space complexity: O(l * m * n)
from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count("0"), s.count("1")] for s in strs]

        @cache
        def dp(i, j, idx):
            if i < 0 or j < 0:
                return float('-inf')

            if idx == len(strs):
                return 0

            return max(dp(i, j, idx+1), 1 + dp(i-counter[idx][0], j-counter[idx][1], idx+1))
        return dp(m, n, 0)

# time complexity: O(l * m * n)
# space complexity: O(l * m * n)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        counter = [[s.count("0"), s.count("1")] for s in strs]
        for zeroes, ones in counter:
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zeroes][j-ones])
        return dp[-1][-1]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(strs, m, n))
strs = ["10", "0", "1"]
m = 1
n = 1
print(Solution().findMaxForm(strs, m, n))
