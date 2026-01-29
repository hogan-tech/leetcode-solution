# time complexity: O(m+n)
# space complexity: O(m)
import heapq
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:
        adjacencyList = [[] for _ in range(26)]
        conversionCount = len(original)
        for i in range(conversionCount):
            adjacencyList[ord(original[i]) - ord("a")].append(
                (ord(changed[i]) - ord("a"), cost[i]))
        minConversionCosts = [self.dijkstra(
            i, adjacencyList) for i in range(26)]
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                charConversionCost = minConversionCosts[
                    ord(s) - ord("a")][ord(t) - ord("a")]
                if charConversionCost == float("inf"):
                    return -1
                totalCost += charConversionCost

        return totalCost

    def dijkstra(
        self, startChar: int, adjacencyList: List[List[tuple]]
    ) -> List[int]:

        priorityQueue = [(0, startChar)]

        minCosts = [float("inf")] * 26

        while priorityQueue:
            currentCost, currentChar = heapq.heappop(priorityQueue)

            if minCosts[currentChar] != float("inf"):
                continue

            minCosts[currentChar] = currentCost

            for targetChar, conversionCost in adjacencyList[currentChar]:
                newTotalCost = currentCost + conversionCost

                if minCosts[targetChar] == float("inf"):
                    heapq.heappush(
                        priorityQueue, (newTotalCost, targetChar)
                    )

        return minCosts


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(Solution().minimumCost(source, target, original, changed, cost))
