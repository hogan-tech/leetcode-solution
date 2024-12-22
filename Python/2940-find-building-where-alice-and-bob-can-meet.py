# time complexity: O(qlogq)
# space complexity: O(n+q)
import heapq
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        maxIdx = []
        results = [-1] * len(queries)
        storeQueries = [[] for _ in heights]

        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                storeQueries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )

        for idx, height in enumerate(heights):

            while maxIdx and maxIdx[0][0] < height:
                _, q_idx = heapq.heappop(maxIdx)
                results[q_idx] = idx

            for element in storeQueries[idx]:
                heapq.heappush(maxIdx, element)

        return results


heights = [6, 4, 8, 5, 2, 7]
queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
print(Solution().leftmostBuildingQueries(heights, queries))
heights = [5, 3, 8, 2, 6, 1, 4, 6]
queries = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
print(Solution().leftmostBuildingQueries(heights, queries))
