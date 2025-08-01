# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         res = []
#         for i in range(numRows):
#             row = [1]
#             for k in range(1, i+1):
#                 row.append(row[-1] * (i + 1 - k) // k)
#             res.append(row)
#         return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0 for _ in range(j)] for j in range(1, numRows+1)]
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


print(Solution().generate(5))
