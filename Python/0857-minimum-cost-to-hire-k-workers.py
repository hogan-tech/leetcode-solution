# time complexity: O(nlogn + nlogk)
# space complexity: O(n + k)
import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        totalCost = float("inf")
        currentTotalQuality = 0
        wageToQualityRatio = []

        for i in range(n):
            wageToQualityRatio.append((wage[i] / quality[i], quality[i]))

        wageToQualityRatio.sort(key=lambda x: x[0])

        highestQualityWorkers = []

        for i in range(n):
            heapq.heappush(highestQualityWorkers, -wageToQualityRatio[i][1])
            currentTotalQuality += wageToQualityRatio[i][1]

            if len(highestQualityWorkers) > k:
                currentTotalQuality += heapq.heappop(highestQualityWorkers)

            if len(highestQualityWorkers) == k:
                totalCost = min(
                    totalCost, currentTotalQuality * wageToQualityRatio[i][0]
                )

        return totalCost


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(Solution().mincostToHireWorkers(quality, wage, k))
