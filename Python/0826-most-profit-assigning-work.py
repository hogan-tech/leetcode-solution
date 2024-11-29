# time complexity: O(nlogn + mlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobProfile = [(0, 0)]
        for i in range(len(difficulty)):
            jobProfile.append((profit[i], difficulty[i]))

        jobProfile.sort(reverse=True)
        for i in range(len(jobProfile) - 1):
            jobProfile[i + 1] = (
                jobProfile[i + 1][0],
                min(jobProfile[i][1], jobProfile[i + 1][1]),
            )

        netProfit = 0
        for ability in worker:
            left, right = 0, len(jobProfile) - 1
            jobProfit = 0
            while left <= right:
                mid = (left + right) // 2
                if jobProfile[mid][1] <= ability:
                    jobProfit = max(jobProfit, jobProfile[mid][0])
                    right = mid - 1
                else:
                    left = mid + 1
            netProfit += jobProfit

        return netProfit


difficulty = [85, 47, 57]
profit = [24, 66, 99]
worker = [40, 25, 25]


print(Solution().maxProfitAssignment(difficulty, profit, worker))
