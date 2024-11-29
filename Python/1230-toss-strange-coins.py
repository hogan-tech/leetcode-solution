# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(target, 0, -1):
                dp[j] = dp[j - 1] * prob[i - 1] + dp[j] * (1 - prob[i - 1])
            dp[0] = dp[0] * (1 - prob[i - 1])
        return dp[target]


prob = [0.4]
target = 1
print(Solution().probabilityOfHeads(prob, target))
