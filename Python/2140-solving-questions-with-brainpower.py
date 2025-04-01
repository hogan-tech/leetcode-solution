# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]


questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
print(Solution().mostPoints(questions))
questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
print(Solution().mostPoints(questions))
