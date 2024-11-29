# time complexity:O(n^3)
# space complexity: O(n^2)
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[0] * len(piles) for _ in range(len(piles))]
        suffixSum = piles[:]

        for i in range(len(suffixSum) - 2, -1, -1):
            suffixSum[i] += suffixSum[i + 1]

        return self.max_stones(suffixSum, 1, 0, memo)

    def max_stones(
        self,
        suffixSum: List[int],
        maxTillNow: int,
        currIndex: int,
        memo: List[List[int]],
    ) -> int:
        if currIndex + 2 * maxTillNow >= len(suffixSum):
            return suffixSum[currIndex]

        if memo[currIndex][maxTillNow] > 0:
            return memo[currIndex][maxTillNow]

        res = float("inf")

        for i in range(1, 2 * maxTillNow + 1):
            res = min(
                res,
                self.max_stones(
                    suffixSum,
                    max(i, maxTillNow),
                    currIndex + i,
                    memo,
                ),
            )

        memo[currIndex][maxTillNow] = suffixSum[currIndex] - res
        return memo[currIndex][maxTillNow]


piles = [2, 7, 9, 4, 4]
print(Solution().stoneGameII(piles))
