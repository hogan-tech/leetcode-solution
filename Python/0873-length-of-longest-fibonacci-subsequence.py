# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        maxLen = 0

        dp = [[0] * n for _ in range(n)]
        valToIdx = {num: idx for idx, num in enumerate(arr)}

        for curr in range(n):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                prevIdx = valToIdx.get(diff, -1)
                dp[prev][curr] = (
                    dp[prevIdx][prev] + 1
                    if diff < arr[prev] and prevIdx >= 0 else 2
                )

                maxLen = max(maxLen, dp[prev][curr])

        return maxLen if maxLen > 2 else 0


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(Solution().lenLongestFibSubseq(arr))
arr = [1, 3, 7, 11, 12, 14, 18]
print(Solution().lenLongestFibSubseq(arr))
