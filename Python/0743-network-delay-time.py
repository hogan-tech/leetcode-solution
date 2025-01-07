# time complexity: O(n + elogn)
# space complexity: O(n+e)
from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        adjList = defaultdict(list)
        for outNode, inNode, time in times:
            adjList[outNode].append((inNode, time))
        minHeap = [(0, k)]
        heapify(minHeap)

        while minHeap:
            currTime, currNode = heappop(minHeap)
            seen.add(currNode)
            if len(seen) == n:
                return currTime
            for neighbor, time in adjList[currNode]:
                if neighbor not in seen:
                    heappush(minHeap, (time + currTime, neighbor))
        return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
times = [[1, 2, 1]]
n = 2
k = 1
print(Solution().networkDelayTime(times, n, k))
times = [[1, 2, 1]]
n = 2
k = 2
print(Solution().networkDelayTime(times, n, k))
