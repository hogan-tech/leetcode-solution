# time complexity: O(k)
# space complexity: O(k)
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)
        i = 0
        for day in range(1, lastDay + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(dp[day - 1] + costs[0],
                              dp[max(0, day-7)] + costs[1],
                              dp[max(0, day-30)] + costs[2]
                              )
        return dp[lastDay]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(Solution().mincostTickets(days, costs))
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
print(Solution().mincostTickets(days, costs))
