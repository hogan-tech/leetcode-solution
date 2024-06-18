from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobsNum = len(profit)
        jobs = []
        totalProfit = 0
        for i in range(jobsNum):
            jobs.append((difficulty[i], profit[i]))
        jobs.sort(key=lambda job: job[1], reverse=True)
        for i in range(len(worker)):
            for j in range(jobsNum):
                if worker[i] >= jobs[j][0]:
                    totalProfit += jobs[j][1]
                    break
        return totalProfit


difficulty = [85, 47, 57]
profit = [24, 66, 99]
worker = [40, 25, 25]


print(Solution().maxProfitAssignment(difficulty, profit, worker))
