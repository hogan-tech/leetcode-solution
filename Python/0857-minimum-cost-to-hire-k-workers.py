# time complexity: O(nlogn + nlogk)
# space complexity: O(n + k)
import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        totalCost = float('inf')
        n = len(quality)
        currTotalQuality = 0
        wageToQualityRatio = []
        for i in range(n):
            wageToQualityRatio.append((wage[i] / quality[i], quality[i]))

        wageToQualityRatio.sort(key=lambda x: x[0])
        maxHeap = []
        for i in range(n):
            heapq.heappush(maxHeap, - wageToQualityRatio[i][1])
            currTotalQuality += wageToQualityRatio[i][1]

            if len(maxHeap) > k:
                currTotalQuality += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                totalCost = min(totalCost, currTotalQuality *
                                wageToQualityRatio[i][0])
        return totalCost


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(Solution().mincostToHireWorkers(quality, wage, k))
quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3
print(Solution().mincostToHireWorkers(quality, wage, k))
