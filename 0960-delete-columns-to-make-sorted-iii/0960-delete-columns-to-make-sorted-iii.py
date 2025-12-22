# time complexity: O(n * w^2)
# space complexity: O(w)
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if all(row[i] <= row[j] for row in strs):
                    dp[i] = max(dp[i], 1 + dp[j])

        return n - max(dp)


strs = ["babca", "bbazb"]
print(Solution().minDeletionSize(strs))
strs = ["edcba"]
print(Solution().minDeletionSize(strs))
strs = ["ghi", "def", "abc"]
print(Solution().minDeletionSize(strs))
