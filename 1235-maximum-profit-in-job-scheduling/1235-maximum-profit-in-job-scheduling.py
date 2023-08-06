from bisect import bisect_left
from typing import List


class Solution:
    def __init__(self):
        self.memo = [-1] * 50001

    def findMaxProfit(self, jobs: List[List[int]], start: List[int], n: int, position: int)->None:
        if position == n:
            return 0
        if self.memo[position] != -1:
            return self.memo[position]
        nextIndex = bisect_left(start, jobs[position][1])
        maxProfit = max(self.findMaxProfit(jobs, start, n, position+1),
                        jobs[position][2] + self.findMaxProfit(jobs, start, n, nextIndex))
        self.memo[position] = maxProfit
        return maxProfit

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        self.memo = [-1]*50001
        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()

        for i in range(len(profit)):
            startTime[i] = jobs[i][0]
        return self.findMaxProfit(jobs, startTime, len(profit), 0)